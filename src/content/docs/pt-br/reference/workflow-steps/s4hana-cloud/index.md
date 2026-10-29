---
title: Etapas do SAP S/4HANA Cloud
description: Etapas de fluxo de trabalho que leem e gravam no SAP S/4HANA Cloud Public Edition por meio da sua conexão do S/4HANA Cloud — importam balancete e itens de lançamento contábil e lançam lançamentos contábeis.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

Etapas de fluxo de trabalho que leem e gravam no SAP S/4HANA Cloud Public Edition por meio da sua [conexão do S/4HANA Cloud](/pt-br/guides/connections/s4hana-cloud/). A etapa de importação busca dados de balancete ou de itens de lançamento contábil sem precisar escrever OData; a etapa de lançamento envia lançamentos contábeis pelo pipeline de gravação ERP compartilhado do PlaidCloud.

## Etapas

- [Import S/4HANA Entity](/pt-br/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) — dados de balancete e de itens de lançamento contábil, com filtros no servidor.
- [S/4HANA: Post Journal Entry](/pt-br/reference/workflow-steps/s4hana-cloud/s4hana-post/) — lança lançamentos contábeis via SOAP, com um lançamento de estorno efetivado para correções.

## Relacionados

- [Conector REST do SAP S/4HANA Cloud](/pt-br/reference/connectors/rest/s4hana-cloud/)
- [Conectar ao SAP S/4HANA Cloud](/pt-br/guides/connections/s4hana-cloud/)
- [Revisar o histórico de lançamentos do ERP](/pt-br/guides/connections/erp-post-history/)
