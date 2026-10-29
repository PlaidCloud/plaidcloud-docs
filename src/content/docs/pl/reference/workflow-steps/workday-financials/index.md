---
title: Kroki Workday Financials
description: Kroki przepływu pracy, które odczytują dane z Workday Financials i zapisują je do niego przez połączenie Workday Financials — import danych przez raport RaaS oraz księgowanie zapisów dziennika.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

Kroki przepływu pracy, które odczytują dane z Workday Financials i zapisują je do niego przez [połączenie Workday Financials](/pl/guides/connections/workday-financials/). Krok importu pobiera dostarczony przez klienta raport Report-as-a-Service (RaaS); krok księgowania księguje zapisy dziennika przez współdzielony potok zapisu ERP PlaidCloud.

## Kroki

- [Import Workday Entity](/pl/reference/workflow-steps/workday-financials/import-workday-entity/) — pobierz raport RaaS, z filtrami parametrów raportu.
- [Workday Financials: Post Journal Entry](/pl/reference/workflow-steps/workday-financials/workday-post/) — księguj zapisy dziennika przez `Submit_Accounting_Journal`, z zaksięgowanym zapisem odwracającym dla korekt.

## Powiązane

- [Konektor Workday Financials](/pl/reference/connectors/rest/workday-financials/)
- [Connect to Workday Financials](/pl/guides/connections/workday-financials/)
- [Review ERP Post History](/pl/guides/connections/erp-post-history/)
