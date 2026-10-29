---
title: Kroki Oracle Fusion
description: Kroki przepływu pracy, które odczytują dane z Oracle Fusion Cloud i zapisują je do niego przez połączenie Oracle Fusion — import sald księgi głównej i partii zapisów dziennika przez OData/BIP lub zbiorczy eksport FBDI oraz księgowanie zapisów dziennika.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

Kroki przepływu pracy, które odczytują dane z Oracle Fusion Cloud i zapisują je do niego przez [połączenie Oracle Fusion](/pl/guides/connections/oracle-fusion/). Dwa kroki importu obsługują różne rozmiary pobrań — bezpośrednie wywołanie OData/BIP do pobrań rutynowych oraz asynchroniczny eksport zbiorczy FBDI/BIP do dużych; krok księgowania księguje partie zapisów dziennika przez wspólny potok zapisu ERP w PlaidCloud.

## Kroki

- [Import Fusion Entity](/pl/reference/workflow-steps/oracle-fusion/import-fusion-entity/) — salda księgi głównej i partie zapisów dziennika, z filtrami zakresu dat, okresów i wartości liczbowych po stronie serwera.
- [Import Fusion Bulk Extract](/pl/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) — te same jednostki, przez asynchroniczne zadanie eksportu FBDI/BIP do dużych pobrań.
- [Oracle Fusion: Post Journal Entry](/pl/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) — księgowanie partii zapisów dziennika księgi głównej przez interfejs księgi głównej FBDI, z zaksięgowanym zapisem odwracającym do korekt.

## Powiązane

- [Konektor Oracle Fusion](/pl/reference/connectors/erp/oracle-fusion/)
- [Połączenie z Oracle Fusion](/pl/guides/connections/oracle-fusion/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
