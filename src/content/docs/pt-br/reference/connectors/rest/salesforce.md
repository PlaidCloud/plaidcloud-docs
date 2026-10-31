---
title: Conector REST do Salesforce
description: Configure uma conexão com a API REST do Salesforce no PlaidCloud com o fluxo de credenciais de cliente OAuth 2.0, teste-a e extraia objetos de CRM para tabelas do projeto com a etapa Salesforce Query Object.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## Documentação da API

A [referência da API REST do Salesforce](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) documenta os endpoints de registros e metadados, e o [Bulk API 2.0 Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) documenta os jobs de consulta em que a etapa [Salesforce: Consultar objeto](/pt-br/reference/workflow-steps/salesforce/query-salesforce-object/) é executada.

Para um passo a passo completo — o aplicativo no lado do Salesforce, o usuário Run As, a criação da conexão e o teste — siga o guia [Conectar ao Salesforce](/pt-br/guides/connections/salesforce/). Esta página é a referência de campos por trás dele.

## Como funciona a autenticação

O conector se autentica com **credenciais de cliente OAuth 2.0**: o PlaidCloud troca a consumer key e o segredo do aplicativo por um token de acesso no endpoint de token da própria org e chama a API como o usuário indicado na configuração **Run As** do aplicativo. Não há login interativo, token de atualização nem certificado para gerenciar.

Duas propriedades dessa troca importam na prática:

- **Um token cobre uma extração inteira.** O PlaidCloud armazena em cache o token de acesso por conexão e ambiente até pouco antes de ele expirar, de modo que uma leitura paginada grande não se autentica novamente a cada página. Um token que o Salesforce deixa de aceitar antes do prazo — revogado, por uma restrição de IP ou por uma mudança na política de sessão — é descartado e substituído uma vez, automaticamente.
- **As solicitações vão para onde o Salesforce indica.** A resposta do token informa a instância da org, e todas as chamadas seguintes são feitas nessa instância, e não no host que você digitou, de modo que a conexão continua funcionando depois de uma mudança de My Domain ou de instância.

A versão da API REST é fixada por conexão, em vez de flutuar, para que uma atualização da org não altere silenciosamente o formato das respostas sob uma etapa salva. As novas conexões usam uma versão atualmente suportada; uma conexão pode ser fixada em outra por meio da API de configuração de conexões, e, se uma versão fixada chegar ao fim da vida útil, o Salesforce responde com HTTP 410 e o PlaidCloud informa qual versão foi descontinuada.

## Configuração

Estes campos aparecem ao criar ou editar uma conexão do Salesforce em **Tools > Connections**.

### Descrição da conta

| Campo | Tipo | Descrição |
|---|---|---|
| Nome da conta | Texto | Nome de exibição desta conexão. |
| Memo | Texto (várias linhas) | Observações opcionais sobre a conexão. |

### Conexão

| Campo | Tipo | Descrição |
|---|---|---|
| Host ou endereço IP | Texto | O host My Domain da org: `mycompany.my.salesforce.com` para produção e Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` para um sandbox. O PlaidCloud adiciona `https://` se você o omitir. |

### Credenciais de autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| ID do cliente | Texto | A consumer key do aplicativo. |
| Segredo do cliente | Senha | O consumer secret do aplicativo. Salvo de forma criptografada; digite um novo valor para alterá-lo ou deixe em branco para manter o valor armazenado. |

### Uso e segurança

| Campo | Tipo | Descrição |
|---|---|---|
| Ativa (permitir acesso) | Alternância | Indica se a conexão pode ser usada. Desmarque para suspender o acesso sem excluir a conexão. |
| Modelo de segurança | Seleção | Quem pode usar a conexão: privada para seus proprietários, membros específicos, grupos de segurança específicos ou todos os membros do espaço de trabalho. |

Cada conexão guarda um conjunto desses valores por ambiente, de modo que uma conexão pode apontar para um sandbox no seu ambiente de desenvolvimento e para a produção no seu ambiente de produção. Teste e defina as credenciais por ambiente.

## Testar conexão

**Testar conexão** faz a troca de token real e informa como as credenciais se autenticam:

| Informado | Por que importa |
|---|---|
| ID da organização | Confirma qual org as credenciais alcançam — a forma mais rápida de detectar uma credencial de sandbox salva em um ambiente de produção. |
| Versão da API | A versão mais alta que esta org suporta. As leituras são executadas na versão fixada na conexão — `v61.0`, a menos que `salesforce_api_version` esteja definido — e não nesta. |
| Usuário Run As | O usuário ao qual toda linha e todo campo que esta conexão retorna estão limitados. Verifique isto antes de confiar nas contagens de linhas de uma extração. |

Um teste que falha indica a causa. As falhas de autenticação informam o status HTTP e pedem que você digite novamente o ID e o segredo do cliente, porque um segredo do cliente não pode ser lido de volta depois de salvo.

## Limitações conhecidas

- **O usuário Run As limita toda leitura, de duas formas diferentes.** As linhas que esse usuário não pode ver simplesmente não aparecem, sem erro nem contagem. Um campo que esse usuário não pode ler faz a consulta inteira falhar. Ambos os casos são abordados em [O usuário Run As limita tudo](/pt-br/guides/connections/salesforce/#o-usuário-run-as-delimita-tudo).
- **Somente leitura.** Este conector extrai dados; ele não grava registros de volta no Salesforce.
- **Alguns tipos de campo não podem ser extraídos** — campos compostos de endereço e geolocalização, blobs `base64`, `encryptedstring` e `anyType`. O seletor de campos da etapa marca cada um deles e informa o motivo. Consulte [Campos que a etapa recusa](/pt-br/reference/workflow-steps/salesforce/query-salesforce-object/#campos-que-a-etapa-recusa).
- **Uma extração não é uma sincronização.** Um registro excluído no Salesforce permanece na tabela de destino.

## Relacionados

- [Conectar ao Salesforce](/pt-br/guides/connections/salesforce/) — passo a passo
- [Salesforce: Consultar objeto](/pt-br/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Criar e gerenciar uma conexão](/pt-br/guides/connections/create-connection/)
