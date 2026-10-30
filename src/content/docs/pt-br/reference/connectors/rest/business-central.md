---
title: Conector REST do Business Central
description: Configure uma conexão com o Microsoft Dynamics 365 Business Central no PlaidCloud com credenciais de cliente do Azure AD para importar entidades OData e lançar linhas de diário geral.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## Documentação da API

A [API OData v2.0 padrão](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) do Business Central documenta as entidades e as opções `$filter`/`$orderby` usadas por este conector.

## Como funciona a autenticação

A conexão se autentica como um aplicativo usando **credenciais de cliente (S2S)** do Entra ID (Azure AD): o ID do cliente e o segredo de um registro de aplicativo são trocados por um token de acesso em `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`, com escopo `https://api.businesscentral.dynamics.com/.default`. Não há login interativo. O registro de aplicativo precisa de permissões de API concedidas ao Business Central (`API.ReadWrite.All` ou um escopo mais restrito emitido pelo seu administrador).

Toda solicitação tem como escopo um **ambiente** (por exemplo, `Production` ou um ambiente de sandbox) e uma **empresa** dentro dele; ambos são definidos na conexão, não escolhidos a cada solicitação.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| ID do cliente | Texto | O ID do aplicativo (cliente) do registro de aplicativo do Entra. |
| Segredo do cliente | Texto | O segredo do cliente do registro de aplicativo. Armazenado de forma criptografada. |
| ID do tenant | Texto | O ID do seu tenant do Azure AD. |
| Ambiente | Texto | O nome do ambiente do Business Central, por exemplo `Production`. |
| Empresa | Texto | O ID da empresa do Business Central em que esta conexão lê e lança. |

## Entidades disponíveis para importação

A etapa **Import Business Central Entity** cobre seis entidades: `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Cada extração oferece filtros do lado do servidor por entidade. Consulte a etapa [Import Business Central Entity](/pt-br/reference/workflow-steps/business-central/import-business-central-entity/) para a referência completa dos campos.

`generalLedgerEntries` é somente leitura e apenas de itens lançados: é a entidade a extrair para um balancete ou para detalhes do razão geral, pois nunca inclui uma linha que ainda esteja em um lote de diário não lançado.

## Lançamento de linhas de diário geral

A etapa **Business Central Post** cria linhas dentro de um lote de diário **existente** e lança esse lote pelo pipeline de gravação de ERP compartilhado do PlaidCloud, verificando que o lote contém apenas as linhas desta solicitação antes de lançar e confirmando o lançamento em `generalLedgerEntries` (não no próprio lote de diário). Consulte a etapa [Business Central: Post General Journal Lines](/pt-br/reference/workflow-steps/business-central/business-central-post/) para a referência dos campos e [Conectar ao Business Central](/pt-br/guides/connections/business-central/) para o passo a passo completo de lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Um único tipo de documento de gravação | Há suporte apenas para lançamento de linhas de diário geral. O fluxo de documentos em rascunho (faturas de venda/compra, Draft → Posted) não é suportado: a ação de lançamento desse fluxo não está definida na documentação publicada da Microsoft. |
| Lança somente em um lote existente | Este conector nunca cria um lote de diário no Business Central; crie-o lá primeiro. |
| Lançamentos simultâneos no mesmo lote | A proteção de idempotência tem escopo por número de documento, não por lote de diário: dois números de documento diferentes lançando ao mesmo tempo no mesmo lote não têm garantia de serialização. |
## Relacionados

- [Conectar ao Business Central (guia)](/pt-br/guides/connections/business-central/) — passo a passo: criar a conexão, testá-la, importar uma entidade e lançar um diário.
- [Import Business Central Entity](/pt-br/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/pt-br/reference/workflow-steps/business-central/business-central-post/)
- [Revisar o histórico de lançamentos de ERP](/pt-br/guides/connections/erp-post-history/)
