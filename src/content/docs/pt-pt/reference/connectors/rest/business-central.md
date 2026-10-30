---
title: Conector REST Business Central
description: Configure uma ligação ao Microsoft Dynamics 365 Business Central no PlaidCloud com credenciais de cliente do Azure AD para importar entidades OData e lançar linhas de diário geral.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## Documentação da API

A [API OData v2.0 padrão](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) do Business Central documenta as entidades e as opções `$filter`/`$orderby` que este conector utiliza.

## Como funciona a autenticação

A ligação autentica-se como uma aplicação através do Entra ID (Azure AD) com **credenciais de cliente (S2S)** — o ID de cliente e o segredo de um registo de aplicação são trocados por um token de acesso em `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`, com o âmbito `https://api.businesscentral.dynamics.com/.default`. Não existe início de sessão interativo. O registo de aplicação precisa de permissões de API concedidas ao Business Central (`API.ReadWrite.All` ou um âmbito mais restrito emitido pelo seu administrador).

Cada pedido está limitado a um **ambiente** (por exemplo, `Production` ou um ambiente de teste) e a uma **empresa** nesse ambiente — ambos são definidos na ligação, não escolhidos por pedido.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| ID do cliente | Texto | O ID da aplicação (cliente) do registo de aplicação Entra. |
| Segredo do cliente | Texto | O segredo de cliente do registo de aplicação. Guardado cifrado. |
| ID do inquilino | Texto | O ID do seu inquilino Azure AD. |
| Ambiente | Texto | O nome do ambiente do Business Central, por exemplo `Production`. |
| Empresa | Texto | O ID da empresa do Business Central em que esta ligação lê e lança. |

## Entidades disponíveis para importação

O passo **Import Business Central Entity** abrange seis entidades: `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Cada extração suporta filtros do lado do servidor por entidade. Consulte [Import Business Central Entity](/pt-pt/reference/workflow-steps/business-central/import-business-central-entity/) para a referência completa dos campos.

`generalLedgerEntries` é só de leitura e contém apenas lançamentos já registados — é a entidade a extrair para um balancete ou para o detalhe do razão geral, uma vez que nunca inclui uma linha ainda pendente num lote de diário não lançado.

## Lançamento de linhas de diário geral

O passo **Business Central Post** cria linhas dentro de um lote de diário **existente** e lança esse lote através do pipeline de escrita ERP partilhado do PlaidCloud, verificando que o lote contém apenas as linhas deste pedido antes de lançar e confirmando o lançamento em `generalLedgerEntries` (e não no próprio lote de diário). Consulte [Business Central: Post General Journal Lines](/pt-pt/reference/workflow-steps/business-central/business-central-post/) para a referência dos campos e [Ligar ao Business Central](/pt-pt/guides/connections/business-central/) para o passo a passo completo do lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Um único tipo de documento de escrita | Só é suportado o lançamento de linhas de diário geral. O fluxo de documentos em rascunho (faturas de venda/compra, Rascunho → Lançado) não é suportado — a ação de lançamento desse fluxo não está definida na documentação publicada pela Microsoft. |
| Lança apenas num lote existente | Este conector nunca cria um lote de diário no Business Central — crie-o primeiro nesse sistema. |
| Lançamentos em simultâneo no mesmo lote | A proteção de idempotência é delimitada pelo número do documento, não pelo lote de diário — não é garantido que dois números de documento diferentes lançados em simultâneo no mesmo lote sejam serializados. |
## Relacionado

- [Ligar ao Business Central (guia)](/pt-pt/guides/connections/business-central/) — passo a passo: criar a ligação, testá-la, importar uma entidade e lançar um diário.
- [Import Business Central Entity](/pt-pt/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/pt-pt/reference/workflow-steps/business-central/business-central-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
