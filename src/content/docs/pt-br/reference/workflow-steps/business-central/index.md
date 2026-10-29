---
title: Etapas do Business Central
description: Etapas de fluxo de trabalho que leem e gravam no Microsoft Dynamics 365 Business Central por meio da sua conexão do Business Central — importam entidades OData e lançam linhas do diário geral.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

Etapas de fluxo de trabalho que leem e gravam no Business Central por meio da sua [conexão do Business Central](/pt-br/guides/connections/business-central/). A etapa de importação busca as entidades OData v2.0 padrão do Business Central sem nenhuma consulta para escrever; a etapa de lançamento lança linhas do diário geral pelo pipeline compartilhado de gravação em ERP do PlaidCloud.

## Etapas

- [Import Business Central Entity](/pt-br/reference/workflow-steps/business-central/import-business-central-entity/) — contas, lançamentos contábeis, clientes, fornecedores, itens e diários, com filtros no servidor.
- [Business Central: Post General Journal Lines](/pt-br/reference/workflow-steps/business-central/business-central-post/) — lance linhas em um lote de diário existente e lance o lote.

## Relacionados

- [Conector REST do Business Central](/pt-br/reference/connectors/rest/business-central/)
- [Conectar ao Business Central](/pt-br/guides/connections/business-central/)
- [Revisar o histórico de lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
