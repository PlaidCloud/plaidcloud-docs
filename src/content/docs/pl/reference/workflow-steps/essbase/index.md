---
title: Kroki Oracle Essbase
description: Kroki przepływu pracy, które odczytują dane z kostki Oracle Essbase przez połączenie Essbase — zapytania MDX na żywo i konspekty wymiarów ładowane do wymiaru PlaidCloud — bezpośrednio z chmury.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

Kroki przepływu pracy, które odczytują dane z Oracle **Essbase** przez [połączenie Oracle Essbase](/pl/guides/connections/essbase/): dane kostki przez zapytanie MDX na żywo oraz konspekt wymiaru ładowany do wymiaru PlaidCloud. Essbase jest osiągany **bezpośrednio z chmury** przez jego REST API — dla tych kroków nie ma ścieżki przez agenta lokalnego.

## Kroki

- [Essbase: zapytanie do kostki](/pl/reference/workflow-steps/essbase/essbase-query/) — uruchom na żywo zapytanie MDX do kostki i zapisz siatkę wyników jako tabelę. Bezpośrednio z chmury.
- [Essbase: odczytaj wymiar](/pl/reference/workflow-steps/essbase/essbase-dimension-read/) — załaduj konspekt wymiaru Essbase do wymiaru PlaidCloud. Bezpośrednio z chmury.

## Powiązane

- [Połączenie z Oracle Essbase (przewodnik)](/pl/guides/connections/essbase/)
- [Złącze Oracle Essbase](/pl/reference/connectors/erp/oracle-essbase/)
