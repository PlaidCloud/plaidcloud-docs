---
title: Resolução de problemas
description: Problemas comuns ao ligar agentes de IA ao servidor MCP do PlaidCloud e como os resolver.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## O Cursor (ou outro cliente restritivo) não consegue ligar-se de todo

Sintoma: o servidor nunca estabelece uma sessão no Cursor e em clientes restritivos semelhantes, enquanto a mesma área de trabalho funciona no Claude Code.

Causa: uma **barra final** no URL do servidor. Utilize `https://<your-workspace>.plaid.cloud/mcp`, e não `.../mcp/`. Os clientes restritivos rejeitam um URL com barra final (ou não seguem o redirecionamento que o caminho anterior emitia), ao passo que clientes mais permissivos, como o Claude Code, toleram-no.

Correção: remova a barra final do `url` na sua configuração e volte a ligar. Todos os exemplos nestes guias utilizam a forma sem barra final.

## «failed to connect» / «session not found»

Sintoma: a configuração do cliente parece correta, mas o servidor aparece como falhado no painel de estado do MCP do cliente. Os registos do servidor mostram erros 404 `Session not found`.

Causa: um erro conhecido em alguns clientes MCP (sobretudo o Claude Code 2.1.111 com cabeçalhos `Authorization` estáticos), em que o cliente não preserva o `mcp-session-id` entre pedidos HTTP sucessivos. O servidor MCP do PlaidCloud funciona em modo HTTP sem estado para contornar esta situação; se a observar num tenant que não foi reimplementado desde a correção, peça ao administrador que o reimplemente.

Até a reimplementação ser concluída, o fluxo OAuth (sem cabeçalhos `Authorization` estáticos) continua a funcionar, pois utiliza um caminho de código diferente no cliente.

## A página «Application Access Request»

Sintoma: depois de iniciar sessão no PlaidCloud durante uma autorização OAuth, chega a uma página intitulada **Application Access Request** que indica uma aplicação e um URI de redirecionamento, e tem de clicar em Approve para o fluxo continuar.

Causa: é o comportamento esperado. Todas as autorizações OAuth através do servidor MCP do PlaidCloud apresentam esta página, para que possa confirmar a que se está a ligar antes de ser emitido um token: indica a aplicação requerente e o URI de redirecionamento para onde as credenciais serão enviadas. Verifique se ambos correspondem ao cliente a que se está realmente a ligar e não aprove um pedido que não iniciou.

Um cliente já ligado não volta a ver esta página quando o token é renovado; apenas uma nova autorização (primeira ligação, ou depois de o token de renovação expirar ou ser revogado) a apresenta de novo.

Correção: não há nada a corrigir; aprove a página para continuar. Se iniciou a autorização num navegador (ou perfil) e a página aparece noutro, não será concluída: o consentimento está associado ao navegador que iniciou o fluxo. Reinicie a autorização a partir do mesmo navegador em que tem a sessão iniciada no PlaidCloud.

## «OAuth flow is not in progress» durante o início de sessão no Claude Code

Sintoma: autoriza no navegador, cola o URL de retorno no Claude Code e este indica que não há nenhum fluxo em curso.

Causa: o estado OAuth em memória da ponte é por porta e pode perder-se entre as chamadas das ferramentas `authenticate` e `complete_authentication`, em particular em sessões remotas/SSH em que o retorno do navegador não consegue alcançar `localhost`.

Correção: mude para o fluxo estático com token Bearer. Abra `https://<your-workspace>.plaid.cloud/mcp/setup/token` num navegador em que tenha a sessão iniciada no PlaidCloud, copie o excerto para o seu `.mcp.json` e reinicie o Claude Code.

## Token expirado

Sintoma: ferramentas que funcionavam ontem devolvem agora 401 Unauthorized.

Causa: os tokens Bearer estáticos seguem a política de duração dos tokens de acesso do seu realm Keycloak (normalmente de algumas horas a um dia).

Correção: volte a carregar `https://<your-workspace>.plaid.cloud/mcp/setup/token` para gerar um token novo e cole-o na sua configuração. Para sessões de longa duração, prefira o OAuth: os clientes que o suportam renovam os tokens automaticamente.

## «No `access_token` in session»

Sintoma: ao abrir `/mcp/setup/token`, é apresentado «Sign-in required» ou «No access_token in session», embora tenha a sessão iniciada no PlaidCloud.

Causa: a sua sessão foi estabelecida por um caminho de início de sessão que não colocou em cache o token do Keycloak (invulgar, mas possível).

Correção: termine a sessão no PlaidCloud e volte a iniciá-la através da página de início de sessão habitual. A nova sessão passará a incluir o token de acesso.

## Ferramentas em falta ou catálogo incompleto

Sintoma: `mcp_introspect` devolve menos ferramentas do que o esperado, ou as ferramentas de que necessita não estão lá.

Causa 1 — âmbitos: as ferramentas exigem âmbitos específicos do PlaidCloud (por exemplo, `analyze.workflow.write`). Se a sua conta não tiver o âmbito, a ferramenta recusa-se a executar. Execute `mcp_introspect(name='<tool>')` para ver os `required_scopes`. Peça ao administrador da área de trabalho que conceda o âmbito, ou execute a operação através de uma conta que o tenha.

Causa 2 — incompatibilidade de versão: uma implementação mais antiga pode não ter todas as ferramentas descritas na documentação mais recente. Compare o número de ferramentas devolvido por `mcp_introspect()` com as notas de versão da sua versão atual; se necessário, peça uma reimplementação.

## Vários tenants: a que tenant acabou de aceder o agente?

Sintoma: tem vários tenants do PlaidCloud configurados e a resposta do agente pode ter vindo de qualquer um deles.

Correção: indique explicitamente o tenant no seu pedido («no tenant **dev**, lista os fluxos de trabalho…»). Os nomes dos servidores MCP que escolheu na configuração (por exemplo, `plaidcloud-prod`, `plaidcloud-dev`) servem também de identificadores que o modelo consegue distinguir. Para operações críticas, mantenha a produção desativada no seletor de conectores até precisar efetivamente dela.

## Limites de taxa e quota

A superfície REST do PlaidCloud tem limite de pedidos por minuto, através do mesmo middleware que serve a interface. As chamadas MCP partilham esse limite. Se um agente disparar uma longa sequência de chamadas `find` (por exemplo, ao tentar enumerar todos os projetos, fluxos de trabalho e passos), pode atingir o limite. Utilize a paginação (`cursor`, `limit`) e `count_only=True` para verificações de dimensão, em vez de obter o conjunto de resultados completo.

Tenha em conta que um find devolve 25 linhas por página por predefinição (`step_find` devolve 50), pelo que enumerar um conjunto grande custa mais chamadas do que antes: aumente `limit` numa pesquisa exaustiva deliberada, em vez de paginar com o valor predefinido. Inversamente, se continuar a atingir o limite, `count_only=True` e uma projeção `fields=[...]` mais restrita significam, em geral, que não precisava da pesquisa exaustiva.

## Uma lista parece curta, ou um agente diz «são todos»

Sintoma: um find devolveu menos linhas do que esperava, ou o agente concluiu que um projeto tem 25 tabelas quando tem 300.

Correção: verifique o envelope. Uma página limitada define `next_cursor` e uma ferramenta find indica também a lista truncada em `truncated`; qualquer um dos dois significa que há mais para obter. `total` indica sempre a contagem completa, por isso compare-o com as linhas que recebeu. Peça ao agente que pagine com o cursor ou que volte a executar com um `limit` mais elevado.

## Um resultado com o aspeto `{"_fmt": "cols", ...}`

Sintoma: uma ferramenta devolveu `{"_fmt": "cols", "cols": [...], "rows": [[...]]}` em vez da lista de objetos que esperava.

Esta é a forma pretendida para um resultado grande cujas linhas têm todas os mesmos campos: os nomes dos campos são enviados uma só vez, em vez de repetidos em cada linha. A linha *i* é `dict(zip(cols, rows[i]))`. Os agentes são informados disto quando se ligam e tratam-no sem necessidade de instruções; se estiver a ler estas respostas a partir do seu próprio código, descodifique as duas formas, porque os resultados pequenos e irregulares continuam a chegar como matrizes normais de objetos. Nada mais no envelope se altera e nenhum valor é modificado. Consulte [Primeiros passos com agentes de programação com IA](/pt-pt/integrations/ai-coding-agents/getting-started/#resultados-orientados-a-colunas).

## Obter ajuda

Para problemas do lado do servidor (falhas de autenticação, ferramentas que devolvem erros sem causa óbvia, ferramentas em falta), verifique primeiro o envelope `error` da resposta. Todas as falhas incluem `code`, `retryable`, `message` e, muitas vezes, uma `hint`. Se a sugestão não for suficiente, contacte o administrador do PlaidCloud ou abra um pedido de suporte com o ID do pedido (devolvido no cabeçalho de resposta `X-Request-Id`).
