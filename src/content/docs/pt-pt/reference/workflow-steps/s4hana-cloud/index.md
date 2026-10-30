---
title: Passos do SAP S/4HANA Cloud
description: Passos de fluxo de trabalho que leem e escrevem no SAP S/4HANA Cloud Public Edition através da ligação S/4HANA Cloud — importam balancete e itens de lançamentos, e lançam lançamentos de diário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

Passos de fluxo de trabalho que leem e escrevem no SAP S/4HANA Cloud Public Edition através da sua [ligação S/4HANA Cloud](/pt-pt/guides/connections/s4hana-cloud/). O passo de importação obtém dados de balancete ou de itens de lançamentos sem necessidade de escrever OData; o passo de lançamento regista lançamentos de diário através do pipeline de escrita ERP partilhado do PlaidCloud.

## Passos

- [Import S/4HANA Entity](/pt-pt/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) — dados de balancete e de itens de lançamentos, com filtros aplicados no servidor.
- [S/4HANA: Post Journal Entry](/pt-pt/reference/workflow-steps/s4hana-cloud/s4hana-post/) — lança lançamentos de diário por SOAP, com um lançamento de reversão registado para correções.

## Ver também

- [SAP S/4HANA Cloud REST Connector](/pt-pt/reference/connectors/rest/s4hana-cloud/)
- [Connect to SAP S/4HANA Cloud](/pt-pt/guides/connections/s4hana-cloud/)
- [Review ERP Post History](/pt-pt/guides/connections/erp-post-history/)
