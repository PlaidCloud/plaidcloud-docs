---
title: Export to ORC
description: Eksportuj tabele projektu PlaidCloud do konta dokumentów jako pliki Apache ORC w postaci kolumnowej, z wybranym kodekiem kompresji.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## Opis

Zapisuje tabele projektu na koncie dokumentów jako pliki [Apache ORC](https://orc.apache.org/), po jednym pliku dla każdej tabeli. ORC to format kolumnowy odczytywany przez Hive, Spark i większość chmurowych platform danych, a schemat jest przechowywany w pliku. Używaj go razem z krokiem [Importuj ORC](/pl/reference/workflow-steps/import/import-orc/).

Formularz kroku zawiera stronę **Parametry pliku** (plik docelowy, prefiks, kompresja i działanie, gdy plik istnieje) oraz stronę **Parametry rekordu**, na której wymieniono eksportowane tabele wraz z wyborem danych tabeli i filtrami danych dla każdej z nich. [Zmigrowane przepływy pracy KNIME](/pl/guides/workflows/migrate-knime-workflows/) używają tego kroku do zapisu plików ORC.

## Konfiguracja

* **Plik docelowy** (`output_file`) — konto dokumentów i folder, do których zapisywane są pliki.
* **Prefiks pliku docelowego** (`file_name`) — prefiks pliku. Każda tabela jest zapisywana jako `<prefix><table name>.orc`.
* **Opcja kompresji** (`compression`) — kodek ORC użyty wewnątrz pliku: **Snappy**, **zlib**, **gzip** (zapisywany jako `zlib`), **Zstandard** lub **LZ4**. Opcja **Brak** zapisuje plik bez kompresji.
* **Parametry rekordu** (`frames`) — eksportowane tabele. Każda ramka zawiera własne ustawienia tabeli; ustawienie tabeli umieszczone na górze kroku zamiast wewnątrz ramki nie jest odczytywane.
  * `id` — etykieta tabeli w ostrzeżeniach.
  * `source` — eksportowana tabela projektu. Od niej pochodzi nazwa każdego pliku.
  * `source_columns` i `target_columns` — odczytywane i zapisywane kolumny, z ewentualną zmianą nazwy, typu i agregacją dla poszczególnych kolumn.
  * `source_where` — filtr wierszy źródłowych.
  * `aggregate` i `aggregation_type` — podsumowanie wierszy; `aggregation_type` to podsumowanie stosowane do kolumn, które nie mają własnego.
  * `having` — filtr podsumowanych wierszy.
  * `distinct` — zapisuje tylko unikalne wiersze.
  * `use_target_slicer`, `limit_target_start` i `limit_target_end` — zapisują tylko wiersze od pozycji początkowej do pozycji końcowej wyniku.
  * `sort_columns` — ustawiane za pomocą asystenta AI lub REST API, aby uporządkować zapisywane wiersze według tych kolumn źródłowych, począwszy od pierwszego klucza, każda jako `{source, ascending, nulls}`. Kolumna klucza nie musi być zapisywana. Wartość `nulls` domyślnie wynosi `first` przy sortowaniu rosnącym i `last` przy malejącym. Nie jest używane z `aggregate` ani `distinct`.
* **Istniejący już plik** (`if_exists`), w sekcji **Jeśli plik istnieje** — **Nadpisz go** (`overwrite`, domyślnie) zastępuje już istniejący plik; **Zakończ krok błędem, nic nie zapisując** (`fail`) zatrzymuje krok, nic nie zapisując, gdy plik, który miałby zostać zapisany, już istnieje.

## Powiązane

- [Kroki eksportu](/pl/reference/workflow-steps/export/)
- [Importuj ORC](/pl/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/pl/reference/workflow-steps/export/export-to-parquet/)
