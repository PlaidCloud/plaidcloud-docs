---
title: Kroki IBM TM1 / Planning Analytics
description: Kroki przepływu pracy, które odczytują dane z serwera IBM TM1 / Planning Analytics przez Twoje połączenie TM1 — dane kostki według zapisanego widoku lub MDX oraz hierarchie wymiarów — bezpośrednio z chmury lub przez lokalnego agenta PlaidLink.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

Kroki przepływu pracy, które odczytują dane z IBM **TM1 / Planning Analytics** przez Twoje [połączenie TM1](/pl/guides/connections/tm1/): dane kostki według zapisanego widoku lub MDX z opcjonalnym wycinkiem punktu widzenia oraz hierarchie wymiarów ładowane do wymiaru PlaidCloud. Łącz się z TM1 bezpośrednio z chmury lub, w przypadku serwera osiągalnego tylko z wnętrza Twojej sieci, przez lokalnego agenta PlaidLink.

## Kroki

- [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — odczytuje kostkę według zapisanego widoku lub MDX, z wycinkiem punktu widzenia i podglądem przed zapisem. Bezpośrednio z chmury.
- [TM1: zapytanie do kostki (agent)](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — lokalny odpowiednik kroku TM1: zapytanie do kostki, przekazywany przez zainstalowanego agenta PlaidLink.
- [TM1: odczytaj wymiar](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — ładuje hierarchię TM1 do wymiaru PlaidCloud. Bezpośrednio z chmury.

## Powiązane

- [Połączenie z TM1 (przewodnik)](/pl/guides/connections/tm1/)
- [Łącznik TM1](/pl/reference/connectors/rest/tm1/)
