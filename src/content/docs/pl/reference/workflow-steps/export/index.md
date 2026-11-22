---
title: Kroki eksportu
description: Kroki przepływu pracy, które zapisują tabele projektu w zewnętrznych miejscach docelowych — formatach plików, kontach dokumentów, zewnętrznych bazach danych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

Kroki przepływu pracy, które zapisują tabele projektu w zewnętrznych miejscach docelowych — formatach plików, kontach dokumentów, zewnętrznych bazach danych.

## Kroki

- [Archiwizuj tabele](/pl/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables](/pl/reference/workflow-steps/export/export-external-tables/)
- [Eksportuj Kafka](/pl/reference/workflow-steps/export/export-kafka/)
- [Eksportuj MongoDB](/pl/reference/workflow-steps/export/export-mongodb/)
- [Eksportuj archiwum projektu](/pl/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table](/pl/reference/workflow-steps/export/export-project-table/)
- [Export Quandl](/pl/reference/workflow-steps/export/export-quandl/)
- [Eksportuj SQL](/pl/reference/workflow-steps/export/export-sql/)
- [Export Templated](/pl/reference/workflow-steps/export/export-templated/)
- [Export to Avro](/pl/reference/workflow-steps/export/export-to-avro/)
- [Export to CSV](/pl/reference/workflow-steps/export/export-to-csv/)
- [Export to Excel](/pl/reference/workflow-steps/export/export-to-excel/)
- [Export to Excel Sheets](/pl/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export to Google Spreadsheet](/pl/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export to HDF](/pl/reference/workflow-steps/export/export-to-hdf/)
- [Export to JSON](/pl/reference/workflow-steps/export/export-to-json/)
- [Export to ORC](/pl/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet](/pl/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF](/pl/reference/workflow-steps/export/export-to-pdf/)
- [Export to Table Archive](/pl/reference/workflow-steps/export/export-to-table-archive/)
- [Export to XML](/pl/reference/workflow-steps/export/export-to-xml/)
- [Księgowanie dokumentów](/pl/reference/workflow-steps/export/post-documents/) — księgowanie tabeli dokumentów w dowolnym skonfigurowanym systemie ERP
- [Eksport pliku przestrzennego](/pl/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/pl/reference/workflow-steps/export/export-hyper/)

## Zapisywane kolumny

Większość kroków eksportu zapisuje wszystkie kolumny tabeli źródłowej w takim kształcie, w jakim tabela wygląda w chwili uruchomienia kroku, w kolejności kolumn tabeli, gdy Data Mapper nie wymienia kolumn docelowych, czyli gdy prawa tabela na karcie **Kolumny** jest pusta. Krok skonfigurowany tylko częściowo eksportuje więc do miejsca docelowego całą tabelę zamiast zakończyć się niepowodzeniem, dlatego przed uruchomieniem eksportu do zewnętrznego miejsca docelowego sprawdź Data Mapper.

Jeśli nie zmapowano kolumn, a tabela źródłowa ich nie ma, eksport CSV, JSON, SQL, Excel, PDF, Google Spreadsheet lub Kafka niczego nie zapisuje i kończy się ostrzeżeniem. W eksporcie kilku tabel, takim jak XML, Parquet, ORC, Avro lub Excel Sheets, taka tabela jest pomijana z ostrzeżeniem wskazującym jej nazwę. Eksportuj MongoDB, Export External Database Tables (krok), Tableau Hyper Export (krok), Eksport pliku przestrzennego (krok) i Run SAP PCM Hyper Loader (krok) działają tak samo: kończą się powodzeniem z ostrzeżeniem wskazującym źródło lub cel, a zewnętrzna tabela zachowuje dotychczasowe wiersze.
