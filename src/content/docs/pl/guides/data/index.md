---
title: Zarządzanie danymi — tabelaryczne
description: Zarządzaj danymi tabelarycznymi w PlaidCloud za pomocą tabel, widoków i wydajnego silnika Lakehouse do przetwarzania danych w dowolnej skali.
sidebar:
  label: Omówienie
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

Warstwa danych PlaidCloud opiera się na **tabelach** (uporządkowanych danych w wierszach i kolumnach) oraz **widokach** (zapisanych zapytaniach do tabel). Obie te struktury istnieją w obrębie projektu i działają na silniku Lakehouse, który skaluje się od małych tabel referencyjnych po analityczne zbiory danych z miliardami wierszy bez zmian w konfiguracji.

## Zawartość tej sekcji

- [Tabele i widoki](/pl/guides/data/tables-views/) — czym jest każde z nich, kiedy którego używać i jak ze sobą współdziałają
- [Eksplorator tabel](/pl/guides/data/table-explorer/) — przeglądaj i sprawdzaj tabele w swoim projekcie
- [Typ danych Currency](/pl/guides/data/currency-data-type/) — dokładny, półszerokościowy typ kolumny dla wartości pieniężnych oraz kiedy wybrać go zamiast typu Numeric
- [Typ danych Vector](/pl/guides/data/vector-data-type/) — przechowuj wstępnie obliczone osadzenia w tabeli projektu, zadeklaruj oczekiwaną szerokość i wyszukuj najbliższe wiersze
- [Migawki tabel](/pl/guides/data/table-snapshots/) — przeglądaj historię migawek, wyświetlaj dane według dawnej migawki oraz cofaj lub przywracaj tabelę
- [Publikowanie danych](/pl/guides/data/publish/) — udostępniaj tabele projektu pulpitom, narzędziom BI i systemom podrzędnym oraz zapoznaj się ze wskazówkami dotyczącymi ich wydajności
- [Wybieranie najnowszego rekordu w dużej tabeli historii](/pl/guides/data/selecting-latest-record-in-large-history-table/) — częsty wzorzec z rozwiązaniem uwzględniającym wydajność
- [Geocoding API](/pl/guides/data/geocoding-api/) — zmigruj integrację geokodowania Google lub Mapbox na punkty końcowe REST geokodowania PlaidCloud
- [Drive-Time Routing API](/pl/guides/data/drive-time-routing-api/) — podgląd dostępny na życzenie: izochrony czasu dojazdu i ranking najbliższych według czasu dojazdu przez REST

## Skąd pochodzą dane

Tabele są zazwyczaj zasilane przez **przepływy pracy** — zautomatyzowane potoki, które importują dane, przekształcają je i zapisują wyniki z powrotem. Zobacz [Przepływy pracy](/pl/guides/workflows/), aby dowiedzieć się, jak je budować, oraz [Dokumentację kroków przepływu pracy](/pl/reference/workflow-steps/), aby poznać każdy dostępny typ kroku.

Informacje o podłączaniu systemów zewnętrznych jako źródeł danych znajdziesz w sekcjach [Połączenia (przewodnik)](/pl/guides/connections/) i [Konektory (dokumentacja)](/pl/reference/connectors/).

## Powiązane

- [Pojęcia](/pl/get-started/concepts/) — jak tabele odnoszą się do przepływów pracy, wymiarów i szerszego modelu danych
- [Projekty](/pl/guides/projects/) — projekty są właścicielami tabel; tabele nie istnieją poza projektem
- [Pulpity](/pl/guides/dashboards/) — korzystają z opublikowanych tabel do wizualizacji
