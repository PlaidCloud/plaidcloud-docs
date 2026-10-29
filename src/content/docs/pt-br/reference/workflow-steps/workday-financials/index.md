---
title: Etapas do Workday Financials
description: Etapas de fluxo de trabalho que leem e gravam no Workday Financials pela sua conexão com o Workday Financials — importar dados por meio de um relatório RaaS e lançar lançamentos contábeis.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

Etapas de fluxo de trabalho que leem e gravam no Workday Financials pela sua [conexão com o Workday Financials](/pt-br/guides/connections/workday-financials/). A etapa de importação extrai um relatório Report-as-a-Service (RaaS) fornecido pelo cliente; a etapa de lançamento registra lançamentos contábeis por meio do pipeline compartilhado de gravação em ERP do PlaidCloud.

## Etapas

- [Import Workday Entity](/pt-br/reference/workflow-steps/workday-financials/import-workday-entity/) — extrai um relatório RaaS, com filtros de parâmetros do relatório.
- [Workday Financials: Post Journal Entry](/pt-br/reference/workflow-steps/workday-financials/workday-post/) — lança lançamentos contábeis por meio de `Submit_Accounting_Journal`, com um lançamento de estorno registrado para correções.

## Relacionados

- [Conector do Workday Financials](/pt-br/reference/connectors/rest/workday-financials/)
- [Conectar ao Workday Financials](/pt-br/guides/connections/workday-financials/)
- [Revisar o histórico de lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
