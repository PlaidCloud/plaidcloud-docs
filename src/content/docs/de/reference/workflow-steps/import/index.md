---
title: Import-Schritte
description: Workflow-Schritte, die Daten aus externen Quellen in Projekttabellen übernehmen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

Workflow-Schritte, die Daten aus externen Quellen in Projekttabellen übernehmen.

Ein Dateiimport prüft die Abfrage, die seine Zieltabelle lädt, bevor er läuft. Eine Abfrage, die mehr als eine einfache SQL-Anweisung über typisierte Spalten enthält, wird abgelehnt, bevor die Zieltabelle erstellt, ersetzt oder geladen wird, sodass die Tabelle genau so bleibt, wie sie war.

Eine fehlende Quelldatei ist kein Fehler. Der Import warnt mit dem Pfad und lässt die Zieltabelle mit ihren deklarierten Spalten leer, sodass spätere Schritte null Zeilen lesen. Das gilt für Importe von CSV, Excel, JSON, fester Breite, YXDB, dBASE, ORC, Avro, Parquet, XML und Db2-Extrakten. Ein XML-Import mit Tags erstellt nur für jedes Tag, das Felder deklariert, eine leere Tabelle. Archiv- und Access-Importe warnen ebenfalls, deklarieren aber keine Spalten und erstellen daher keine Tabelle. Ein Archivimport, der seine Dateien über eine Dokumentensuche findet, gibt keine Warnung zu fehlenden Dateien aus.

Dasselbe gilt, bevor ein Schritt läuft. **Übernehmen** bei der Zuordnung eines Dateiimports sowie das Lesen der Spalten einer Datei über die REST-API oder einen KI-Assistenten antworten mit *Nichts zu befüllen* (über die API mit einer leeren Spaltenliste) und einer Warnung, die den Pfad nennt, wenn die Datei fehlt oder leer ist, statt mit einem Fehler. Der Import einer fehlenden Datei aus Documents in eine neue Tabelle oder einen neuen Schritt erstellt nichts, markiert die Datei als **übersprungen** und zeigt eine Warnung, die den Pfad nennt.

## Schritte

- [Access importieren](/de/reference/workflow-steps/import/import-access/)
- [Alteryx YXDB importieren](/de/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Archiv importieren](/de/reference/workflow-steps/import/import-archive/)
- [Avro importieren](/de/reference/workflow-steps/import/import-avro/)
- [CSV importieren](/de/reference/workflow-steps/import/import-csv/)
- [Delta Lake importieren](/de/reference/workflow-steps/import/import-delta/)
- [DB2-Extrakt importieren](/de/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE](/de/reference/workflow-steps/import/import-dbf/)
- [Excel importieren](/de/reference/workflow-steps/import/import-excel/)
- [Import Delimited](/de/reference/workflow-steps/import/import-delimited/)
- [Externe Datenbanktabellen importieren](/de/reference/workflow-steps/import/import-external-database-tables/)
- [Feste Breite importieren](/de/reference/workflow-steps/import/import-fixed-width/)
- [Import Google BigQuery](/de/reference/workflow-steps/import/import-google-bigquery/)
- [Google Spreadsheet importieren](/de/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF](/de/reference/workflow-steps/import/import-hdf/)
- [JSON importieren](/de/reference/workflow-steps/import/import-json/)
- [Kafka importieren](/de/reference/workflow-steps/import/import-kafka/)
- [Monday importieren](/de/reference/workflow-steps/import/import-monday/)
- [MongoDB importieren](/de/reference/workflow-steps/import/import-mongodb/)
- [ORC importieren](/de/reference/workflow-steps/import/import-orc/)
- [Parquet importieren](/de/reference/workflow-steps/import/import-parquet/)
- [Import Project Table](/de/reference/workflow-steps/import/import-project-table/)
- [Import Quandl](/de/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source](/de/reference/workflow-steps/import/import-singer/)
- [Import SPSS](/de/reference/workflow-steps/import/import-spss/)
- [SQL importieren](/de/reference/workflow-steps/import/import-sql/)
- [Import Stata](/de/reference/workflow-steps/import/import-stata/)
- [XML importieren](/de/reference/workflow-steps/import/import-xml/)
- [Tabellen wiederherstellen](/de/reference/workflow-steps/import/restore-tables/)
