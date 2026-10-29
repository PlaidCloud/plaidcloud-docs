---
title: Kroki Business Central
description: Kroki przepływu pracy odczytujące i zapisujące dane w Microsoft Dynamics 365 Business Central przez połączenie Business Central — importują jednostki OData i księgują wiersze dziennika ogólnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

Kroki przepływu pracy odczytujące i zapisujące dane w Business Central przez [połączenie Business Central](/pl/guides/connections/business-central/). Krok importu pobiera standardowe jednostki OData v2.0 z Business Central bez pisania zapytania; krok księgowania księguje wiersze dziennika ogólnego przez wspólny potok zapisu ERP w PlaidCloud.

## Kroki

- [Krok Import Business Central Entity](/pl/reference/workflow-steps/business-central/import-business-central-entity/) — konta, zapisy księgowe, klienci, dostawcy, towary i dzienniki, z filtrami po stronie serwera.
- [Business Central: zaksięguj dziennik ogólny](/pl/reference/workflow-steps/business-central/business-central-post/) — księguj wiersze w istniejącej partii dziennika i zaksięguj partię.

## Powiązane

- [Konektor REST Business Central](/pl/reference/connectors/rest/business-central/)
- [Połączenie z Business Central](/pl/guides/connections/business-central/)
- [Przeglądanie historii księgowań ERP](/pl/guides/connections/erp-post-history/)
