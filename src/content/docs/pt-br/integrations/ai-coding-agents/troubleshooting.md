---
title: Solução de problemas
description: Problemas comuns ao conectar agentes de IA ao servidor MCP do PlaidCloud e como resolvê-los.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## O Cursor (ou outro cliente rigoroso) não consegue se conectar

Sintoma: o servidor nunca estabelece uma sessão no Cursor e em clientes rigorosos semelhantes, enquanto o mesmo espaço de trabalho funciona no Claude Code.

Causa: uma **barra final** na URL do servidor. Use `https://<your-workspace>.plaid.cloud/mcp`, e não `.../mcp/`. Clientes rigorosos rejeitam uma URL com barra final (ou não seguem o redirecionamento emitido pelo caminho mais antigo), enquanto clientes tolerantes, como o Claude Code, a aceitam.

Solução: remova a barra final do `url` na sua configuração e reconecte. Todos os exemplos destes guias usam a forma sem barra.

## "failed to Connect" / "session Not Found"

Sintoma: a configuração do cliente parece correta, mas o servidor aparece como com falha no painel de status do MCP do cliente. Os logs do servidor mostram erros 404 `Session not found`.

Causa: um bug conhecido em alguns clientes MCP (principalmente o Claude Code 2.1.111 com cabeçalhos `Authorization` estáticos) em que o cliente não preserva o `mcp-session-id` entre requisições HTTP sucessivas. O servidor MCP do PlaidCloud é executado no modo HTTP sem estado para contornar esse problema. Se você estiver vendo o erro em um tenant que não foi reimplantado desde a correção, peça ao seu administrador que faça a reimplantação.

Até que a reimplantação seja concluída, o fluxo OAuth (sem cabeçalhos `Authorization` estáticos) continua funcionando, pois usa um caminho de código diferente no cliente.

## A página "application Access Request"

Sintoma: depois de fazer login no PlaidCloud durante uma autorização OAuth, você chega a uma página intitulada **Application Access Request** que cita um aplicativo e um URI de redirecionamento, e precisa clicar em Approve para que o fluxo continue.

Causa: isso é esperado. Toda autorização OAuth pelo servidor MCP do PlaidCloud mostra essa página para que você confirme a que está se conectando antes de receber um token. Ela informa o aplicativo solicitante e o URI de redirecionamento para o qual as credenciais serão enviadas. Verifique se ambos correspondem ao cliente que você realmente está conectando e não aprove uma solicitação que você não iniciou.

Um cliente já conectado não vê essa página novamente na renovação do token. Somente uma nova autorização (primeira conexão, ou depois que o token de atualização expira ou é revogado) volta a exibi-la.

Solução: não há nada a corrigir. Aprove a página para continuar. Se você iniciou a autorização em um navegador (ou perfil) e a página está sendo exibida em outro, ela não será concluída: o consentimento está vinculado ao navegador que iniciou o fluxo. Reinicie a autorização no mesmo navegador em que você está conectado ao PlaidCloud.

## "oauth Flow is Not in Progress" durante o login no Claude Code

Sintoma: você autoriza no navegador, cola a URL de retorno no Claude Code e ele informa que nenhum fluxo está em andamento.

Causa: o estado OAuth em memória da ponte é por porta e pode ser perdido entre as chamadas das ferramentas `authenticate` e `complete_authentication`, principalmente em sessões remotas/SSH em que o retorno do navegador não alcança `localhost`.

Solução: mude para o fluxo Bearer estático. Abra `https://<your-workspace>.plaid.cloud/mcp/setup/token` em um navegador em que você esteja conectado ao PlaidCloud, copie o trecho para o seu `.mcp.json` e reinicie o Claude Code.

## Token expirado

Sintoma: ferramentas que funcionavam ontem agora retornam 401 Unauthorized.

Causa: os tokens Bearer estáticos seguem a política de tempo de vida do token de acesso do seu realm do Keycloak (normalmente de algumas horas a um dia).

Solução: recarregue `https://<your-workspace>.plaid.cloud/mcp/setup/token` para gerar um novo token e cole-o na sua configuração. Para sessões de longa duração, prefira o OAuth: os clientes que o suportam renovam os tokens automaticamente.

## "no `access_token` in Session"

Sintoma: ao abrir `/mcp/setup/token`, aparece "Sign-in required" ou "No access_token in session", mesmo com você conectado ao PlaidCloud.

Causa: sua sessão foi estabelecida por um caminho de login que não armazenou em cache o token do Keycloak (incomum, mas possível).

Solução: saia do PlaidCloud e entre novamente pela página de login padrão. A nova sessão terá o token de acesso.

## Ferramentas ausentes ou catálogo incompleto

Sintoma: `mcp_introspect` retorna menos ferramentas do que o esperado, ou ferramentas específicas de que você precisa não estão lá.

Causa 1, escopos: as ferramentas exigem escopos específicos do PlaidCloud (por exemplo, `analyze.workflow.write`). Se a sua conta não tiver o escopo, a ferramenta se recusará a executar. Execute `mcp_introspect(name='<tool>')` para ver `required_scopes`. Peça ao administrador do seu espaço de trabalho que conceda o escopo ou execute a operação com uma conta que o tenha.

Causa 2, incompatibilidade de versão: uma implantação mais antiga pode não ter todas as ferramentas descritas na documentação mais recente. Compare a contagem de ferramentas de `mcp_introspect()` com as notas de versão da sua versão atual e peça uma reimplantação, se necessário.

## Multi-tenant: qual tenant o agente acabou de acessar?

Sintoma: você tem vários tenants do PlaidCloud configurados e a resposta do agente poderia ter vindo de qualquer um deles.

Solução: inclua o tenant explicitamente no seu prompt ("no tenant **dev**, liste os fluxos de trabalho…"). Os nomes de servidor MCP que você escolheu na configuração (por exemplo, `plaidcloud-prod`, `plaidcloud-dev`) também funcionam como identificadores que o modelo pode usar para diferenciá-los. Em operações de alto risco, mantenha a produção desativada no seletor de conectores até precisar dela.

## Limites de taxa e cota

A superfície REST do PlaidCloud tem limite de requisições por minuto, aplicado pelo mesmo middleware que atende a interface. As chamadas MCP compartilham esse limite. Se um agente disparar uma longa sequência de chamadas `find` (por exemplo, tentando enumerar todos os projetos, fluxos de trabalho e etapas), você pode atingir o limite. Use paginação (`cursor`, `limit`) e `count_only=True` para verificações de tamanho, em vez de buscar o conjunto completo de resultados.

Observe que um find retorna 25 linhas por página por padrão (`step_find` retorna 50), portanto enumerar um conjunto grande custa mais chamadas do que antes: aumente `limit` em uma varredura deliberada, em vez de paginar com o valor padrão. Por outro lado, se você continua atingindo o limite, `count_only=True` e uma projeção `fields=[...]` mais restrita geralmente indicam que a varredura não era necessária.

## Uma lista parece curta, ou um agente diz "isso é tudo"

Sintoma: um find retornou menos linhas do que você esperava, ou o agente concluiu que um projeto tem 25 tabelas quando ele tem 300.

Solução: verifique o envelope. Uma página limitada define `next_cursor`, e uma ferramenta find também nomeia a lista cortada em `truncated`; qualquer um dos dois significa que há mais a buscar. `total` informa a contagem completa em qualquer caso, portanto compare-o com as linhas que você recebeu. Peça ao agente que pagine com o cursor ou que execute novamente com um `limit` maior.

## Um resultado se parece com `{"_fmt": "cols", ...}`

Sintoma: uma ferramenta retornou `{"_fmt": "cols", "cols": [...], "rows": [[...]]}` em vez da lista de objetos que você esperava.

Esse é o formato pretendido para um resultado grande cujas linhas têm todas os mesmos campos: os nomes dos campos são enviados uma única vez, em vez de repetidos em cada linha. A linha *i* é `dict(zip(cols, rows[i]))`. Os agentes são informados sobre isso quando se conectam e lidam com o formato sem precisar de instruções; se você estiver lendo essas respostas a partir do seu próprio código, decodifique os dois formatos, pois resultados pequenos e irregulares ainda chegam como arrays comuns de objetos. Nada mais no envelope muda e nenhum valor é alterado. Consulte [Introdução aos agentes de codificação com IA](/pt-br/integrations/ai-coding-agents/getting-started/#resultados-orientados-a-colunas).

## Como obter ajuda

Para problemas do lado do servidor, como falhas de autenticação, ferramentas que retornam erros sem causa óbvia ou ferramentas ausentes, verifique primeiro o envelope `error` da resposta. Toda falha inclui `code`, `retryable`, `message` e, muitas vezes, um `hint`. Se a dica não for suficiente, entre em contato com o administrador do PlaidCloud ou abra um chamado de suporte com o ID da requisição (retornado no cabeçalho de resposta `X-Request-Id`).
