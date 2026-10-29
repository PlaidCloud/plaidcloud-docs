---
title: Etapas do Dynamics 365 F&O
description: "Etapas de fluxo de trabalho que leem e gravam no Dynamics 365 Finance & Operations por meio da sua conexão do D365 F&O: importar entidades OData/DMF e lançar lançamentos contábeis."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

Etapas de fluxo de trabalho que leem e gravam no Dynamics 365 Finance & Operations (D365 F&O) por meio da sua [conexão do D365 F&O](/pt-br/guides/connections/dynamics-365-fo/). A etapa de importação busca entidades OData ou extrações em massa DMF sem precisar escrever OData; a etapa de lançamento lança lançamentos contábeis do razão geral pelo pipeline compartilhado de gravação em ERP do PlaidCloud.

## Etapas

- [Import D365 F&O Entity](/pt-br/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — dados mestres e cabeçalhos de diário, no modo OData ou DMF em massa, com filtros no servidor.
- [D365 F&O: Post Journal Entry](/pt-br/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — lança lançamentos contábeis do razão geral, com um lançamento de estorno para correções.

## Relacionados

- [Conector REST do Dynamics 365 F&O](/pt-br/reference/connectors/rest/dynamics-365-fo/)
- [Conectar-se ao Dynamics 365 Finance & Operations](/pt-br/guides/connections/dynamics-365-fo/)
- [Revisar o histórico de lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
