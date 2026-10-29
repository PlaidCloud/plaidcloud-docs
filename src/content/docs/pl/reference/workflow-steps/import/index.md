---
title: Kroki importu
description: Kroki przepływu pracy, które wprowadzają dane z zewnętrznych źródeł do tabel projektu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

Kroki przepływu pracy, które wprowadzają dane z zewnętrznych źródeł do tabel projektu.

Import pliku sprawdza zapytanie, które ładuje jego tabelę docelową, zanim zostanie uruchomione. Zapytanie zawierające cokolwiek innego niż zwykła instrukcja SQL na typowanych kolumnach jest odrzucane, zanim tabela docelowa zostanie utworzona, zastąpiona lub załadowana, więc tabela pozostaje dokładnie taka, jaka była.

Brakujący plik źródłowy nie jest błędem. Import wyświetla ostrzeżenie ze ścieżką i pozostawia tabelę docelową pustą, z zadeklarowanymi kolumnami, dzięki czemu kolejne kroki odczytują zero wierszy. Dotyczy to importów CSV, Excel, JSON, plików o stałej szerokości, YXDB, dBASE, ORC, Avro, Parquet, XML oraz wyodrębnień Db2. Import XML ze znacznikami tworzy pustą tabelę tylko dla każdego znacznika, który deklaruje pola. Importy archiwów i Access również wyświetlają ostrzeżenie, ale nie deklarują kolumn, więc nie tworzą tabeli. Import archiwum, który znajduje pliki przez wyszukiwanie dokumentów, nie wyświetla ostrzeżenia o brakującym pliku.

To samo dotyczy czasu przed uruchomieniem kroku. **Wypełnij** w mapowaniu importu pliku oraz odczyt kolumn pliku przez REST API lub asystenta AI odpowiadają *Brak danych do wypełnienia* (pusta lista kolumn w API) z ostrzeżeniem wskazującym ścieżkę, gdy plik nie istnieje lub jest pusty, zamiast błędu. Import brakującego pliku do nowej tabeli lub kroku z Dokumentów niczego nie tworzy, oznacza plik jako **pominięto** i wyświetla ostrzeżenie wskazujące ścieżkę.

## Kroki

- [Importuj Access](/pl/reference/workflow-steps/import/import-access/)
- [Importuj Alteryx YXDB](/pl/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Importuj archiwum](/pl/reference/workflow-steps/import/import-archive/)
- [Importuj Avro](/pl/reference/workflow-steps/import/import-avro/)
- [Importuj CSV](/pl/reference/workflow-steps/import/import-csv/)
- [Importuj Delta Lake](/pl/reference/workflow-steps/import/import-delta/)
- [Importuj wyodrębnienie DB2](/pl/reference/workflow-steps/import/import-db2-extract/)
- [Krok Import dBASE](/pl/reference/workflow-steps/import/import-dbf/)
- [Importuj Excel](/pl/reference/workflow-steps/import/import-excel/)
- [Krok Import Delimited](/pl/reference/workflow-steps/import/import-delimited/)
- [Importuj zewnętrzne tabele bazy danych](/pl/reference/workflow-steps/import/import-external-database-tables/)
- [Importuj plik o stałej szerokości](/pl/reference/workflow-steps/import/import-fixed-width/)
- [Krok Import Google BigQuery](/pl/reference/workflow-steps/import/import-google-bigquery/)
- [Importuj Arkusz kalkulacyjny Google](/pl/reference/workflow-steps/import/import-google-spreadsheet/)
- [Krok Import HDF](/pl/reference/workflow-steps/import/import-hdf/)
- [Importuj JSON](/pl/reference/workflow-steps/import/import-json/)
- [Importuj Kafka](/pl/reference/workflow-steps/import/import-kafka/)
- [Importuj Monday](/pl/reference/workflow-steps/import/import-monday/)
- [Importuj MongoDB](/pl/reference/workflow-steps/import/import-mongodb/)
- [Importuj ORC](/pl/reference/workflow-steps/import/import-orc/)
- [Importuj Parquet](/pl/reference/workflow-steps/import/import-parquet/)
- [Krok Import Project Table](/pl/reference/workflow-steps/import/import-project-table/)
- [Krok Import Quandl](/pl/reference/workflow-steps/import/import-quandl/)
- [Krok Import Singer Source](/pl/reference/workflow-steps/import/import-singer/)
- [Krok Import SPSS](/pl/reference/workflow-steps/import/import-spss/)
- [Importuj SQL](/pl/reference/workflow-steps/import/import-sql/)
- [Krok Import Stata](/pl/reference/workflow-steps/import/import-stata/)
- [Importuj XML](/pl/reference/workflow-steps/import/import-xml/)
- [Przywróć tabele](/pl/reference/workflow-steps/import/restore-tables/)
