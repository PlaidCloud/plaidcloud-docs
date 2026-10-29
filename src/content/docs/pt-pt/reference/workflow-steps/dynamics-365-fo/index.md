---
title: Passos Dynamics 365 F&O
description: Passos de fluxo de trabalho que leem e escrevem no Dynamics 365 Finance & Operations através da sua ligação D365 F&O — importar entidades OData/DMF e lançar lançamentos de diário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

Passos de fluxo de trabalho que leem e escrevem no Dynamics 365 Finance & Operations (D365 F&O) através da sua [ligação D365 F&O](/pt-pt/guides/connections/dynamics-365-fo/). O passo de importação obtém entidades OData ou extrações em massa DMF sem necessidade de escrever OData; o passo de lançamento lança lançamentos de diário do razão geral através do pipeline partilhado de escrita ERP do PlaidCloud.

## Passos

- [Import D365 F&O Entity](/pt-pt/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — dados mestre e cabeçalhos de diário, em modo OData ou DMF em massa, com filtros no servidor.
- [D365 F&O: Post Journal Entry](/pt-pt/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — lança lançamentos de diário do razão geral, com um lançamento de estorno efetuado para correções.

## Relacionado

- [Conector REST do Dynamics 365 F&O](/pt-pt/reference/connectors/rest/dynamics-365-fo/)
- [Ligar ao Dynamics 365 Finance & Operations](/pt-pt/guides/connections/dynamics-365-fo/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
