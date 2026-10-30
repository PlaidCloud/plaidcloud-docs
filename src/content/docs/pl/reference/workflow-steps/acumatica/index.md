---
title: Kroki Acumatica
description: Kroki przepływu pracy, które odczytują dane z Acumatica i zapisują je w Acumatica przez Połączenie Acumatica — importują jednostki contract-based REST oraz księgują zapisy dziennika, faktury, rachunki i płatności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

Kroki przepływu pracy, które odczytują dane z Acumatica i zapisują je w Acumatica przez [Połączenie Acumatica](/pl/guides/connections/acumatica/). Krok importu pobiera jednostki contract-based REST Acumatica bez pisania OData; krok księgowania księguje zapisy dziennika, faktury sprzedaży, rachunki i płatności za pośrednictwem wspólnego potoku zapisu ERP PlaidCloud.

## Kroki

- [Import Acumatica Entity](/pl/reference/workflow-steps/acumatica/import-acumatica-entity/) — dane główne i jednostki transakcyjne, z filtrami po stronie serwera.
- [Acumatica: Post Documents](/pl/reference/workflow-steps/acumatica/acumatica-post/) — księgowanie zapisów dziennika, faktur sprzedaży, rachunków i płatności.

## Powiązane

- [Konektor Acumatica REST](/pl/reference/connectors/rest/acumatica/)
- [Połączenie z Acumatica](/pl/guides/connections/acumatica/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
