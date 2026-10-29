---
title: Passos Business Central
description: Passos de fluxo de trabalho que leem e escrevem no Microsoft Dynamics 365 Business Central através da sua ligação Business Central — importar entidades OData e lançar linhas do diário geral.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

Passos de fluxo de trabalho que leem e escrevem no Business Central através da sua [ligação Business Central](/pt-pt/guides/connections/business-central/). O passo de importação obtém as entidades OData v2.0 padrão do Business Central sem necessidade de escrever consultas; o passo de lançamento lança linhas do diário geral através do pipeline partilhado de escrita ERP do PlaidCloud.

## Passos

- [Import Business Central Entity](/pt-pt/reference/workflow-steps/business-central/import-business-central-entity/) — contas, movimentos do razão, clientes, fornecedores, artigos e diários, com filtros do lado do servidor.
- [Business Central: Post General Journal Lines](/pt-pt/reference/workflow-steps/business-central/business-central-post/) — lance linhas num lote de diário existente e lance o lote.

## Relacionado

- [Conector REST do Business Central](/pt-pt/reference/connectors/rest/business-central/)
- [Ligar ao Business Central](/pt-pt/guides/connections/business-central/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
