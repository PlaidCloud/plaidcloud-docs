---
title: Passos do Workday Financials
description: Passos de fluxo de trabalho que leem do Workday Financials e escrevem nele através da ligação ao Workday Financials — importar dados através de um relatório RaaS e lançar diários contabilísticos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

Passos de fluxo de trabalho que leem do Workday Financials e escrevem nele através da sua [ligação ao Workday Financials](/pt-pt/guides/connections/workday-financials/). O passo de importação obtém um relatório Report-as-a-Service (RaaS) fornecido pelo cliente; o passo de lançamento lança diários contabilísticos através do pipeline de escrita ERP partilhado do PlaidCloud.

## Passos

- [Import Workday Entity](/pt-pt/reference/workflow-steps/workday-financials/import-workday-entity/) — obtém um relatório RaaS, com filtros de parâmetros do relatório.
- [Workday Financials: Post Journal Entry](/pt-pt/reference/workflow-steps/workday-financials/workday-post/) — lança diários contabilísticos através de `Submit_Accounting_Journal`, com um lançamento de reversão lançado para correções.

## Relacionado

- [Conector Workday Financials](/pt-pt/reference/connectors/rest/workday-financials/)
- [Ligar ao Workday Financials](/pt-pt/guides/connections/workday-financials/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
