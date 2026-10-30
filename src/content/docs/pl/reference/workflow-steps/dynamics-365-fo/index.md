---
title: Kroki Dynamics 365 F&O
description: Kroki przepływu pracy, które odczytują dane z Dynamics 365 Finance & Operations i zapisują je tam przez połączenie D365 F&O — importują jednostki OData/DMF i księgują zapisy dziennika.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

Kroki przepływu pracy, które odczytują dane z Dynamics 365 Finance & Operations (D365 F&O) i zapisują je tam przez [połączenie D365 F&O](/pl/guides/connections/dynamics-365-fo/). Krok importu pobiera jednostki OData lub zbiorcze wyodrębnienia DMF bez pisania OData; krok księgowania księguje zapisy dziennika księgi głównej przez wspólny potok zapisu ERP w PlaidCloud.

## Kroki

- [Import D365 F&O Entity (krok)](/pl/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — dane główne i nagłówki zapisów dziennika, w trybie OData lub zbiorczym DMF, z filtrami po stronie serwera.
- [D365 F&O: Post Journal Entry (krok)](/pl/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — księguj zapisy dziennika księgi głównej, z zaksięgowanym zapisem odwracającym dla korekt.

## Powiązane

- [Złącze REST Dynamics 365 F&O](/pl/reference/connectors/rest/dynamics-365-fo/)
- [Połączenie z Dynamics 365 Finance & Operations](/pl/guides/connections/dynamics-365-fo/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
