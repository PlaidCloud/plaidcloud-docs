---
title: Zarządzanie danymi — dane tabelaryczne
description: Zarządzaj danymi tabelarycznymi w PlaidCloud za pomocą tabel, widoków i wydajnego silnika Lakehouse, który przetwarza dane w dowolnej skali.
sidebar:
  label: Omówienie
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

Warstwa danych PlaidCloud opiera się na **tabelach** (uporządkowanych danych w wierszach i kolumnach) oraz **widokach** (zapisanych zapytaniach do tabel). Jedne i drugie znajdują się w projekcie i działają na silniku Lakehouse, który skaluje się od małych tabel referencyjnych po analityczne zbiory danych z miliardami wierszy bez zmian w konfiguracji.

## Zawartość tej sekcji

- [Tabele i widoki](/pl/guides/data/tables-views/) — czym są, kiedy używać jednych, a kiedy drugich, i jak ze sobą współdziałają
- [Eksplorator tabel](/pl/guides/data/table-explorer/) — przeglądaj i sprawdzaj tabele w projekcie
- [Typ danych Currency](/pl/guides/data/currency-data-type/) — dokładny typ kolumny o połowie szerokości dla wartości pieniężnych oraz kiedy wybrać go zamiast typu Numeric
- [Typ danych Vector](/pl/guides/data/vector-data-type/) — przechowuj wstępnie obliczone osadzenia w tabeli projektu, zadeklaruj oczekiwaną szerokość i wyszukuj najbliższe wiersze
- [Migawki tabel](/pl/guides/data/table-snapshots/) — przeglądaj historię migawek, wyświetlaj dane według dawnej migawki oraz cofaj lub przywracaj tabelę
- [Okno Lakehouse](/pl/guides/data/lakehouse-window/) — obserwuj i profiluj zapytania, przeglądaj katalogi i tabele wraz z ich migawkami oraz kopiuj zapytanie z podróżą w czasie
- [Publikowanie danych](/pl/guides/data/publish/) — udostępniaj tabele projektu pulpitom, narzędziom BI i systemom podrzędnym oraz zapoznaj się ze wskazówkami dotyczącymi ich wydajności
- [Wybieranie najnowszego rekordu w dużej tabeli historii](/pl/guides/data/selecting-latest-record-in-large-history-table/) — częsty wzorzec z rozwiązaniem uwzględniającym wydajność
- [Geocoding API](/pl/guides/data/geocoding-api/) — przenieś integrację geokodowania Google lub Mapbox na punkty końcowe REST geokodowania PlaidCloud
- [Drive-Time Routing API](/pl/guides/data/drive-time-routing-api/) — wersja zapoznawcza dostępna na życzenie: izochrony czasu dojazdu i ranking najbliższych lokalizacji według czasu dojazdu przez REST

## Skąd pochodzą dane

Tabele są zazwyczaj zasilane przez **przepływy pracy** — zautomatyzowane potoki, które importują dane, przekształcają je i zapisują wyniki. Zobacz [Przepływy pracy](/pl/guides/workflows/), aby dowiedzieć się, jak je budować, oraz [Dokumentację kroków przepływu pracy](/pl/reference/workflow-steps/), aby poznać każdy dostępny typ kroku.

Informacje o podłączaniu systemów zewnętrznych jako źródeł danych znajdziesz w sekcjach [Połączenia (przewodnik)](/pl/guides/connections/) i [Konektory (dokumentacja)](/pl/reference/connectors/).

## Powiązane

- [Pojęcia](/pl/get-started/concepts/) — jak tabele odnoszą się do przepływów pracy, wymiarów i szerszego modelu danych
- [Projekty](/pl/guides/projects/) — projekty są właścicielami tabel; tabele nie istnieją poza projektem
- [Pulpity](/pl/guides/dashboards/) — korzystają z opublikowanych tabel do wizualizacji
