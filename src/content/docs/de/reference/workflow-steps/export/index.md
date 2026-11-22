---
title: Export-Schritte
description: Workflow-Schritte, die Projekttabellen in externe Ziele schreiben — Dateiformate, Dokumentenkonten, externe Datenbanken.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

Workflow-Schritte, die Projekttabellen in externe Ziele schreiben — Dateiformate, Dokumentenkonten, externe Datenbanken.

## Schritte

- [Tabellen archivieren](/de/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables](/de/reference/workflow-steps/export/export-external-tables/)
- [Kafka exportieren](/de/reference/workflow-steps/export/export-kafka/)
- [MongoDB exportieren](/de/reference/workflow-steps/export/export-mongodb/)
- [Projektarchiv exportieren](/de/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table](/de/reference/workflow-steps/export/export-project-table/)
- [Export Quandl](/de/reference/workflow-steps/export/export-quandl/)
- [SQL exportieren](/de/reference/workflow-steps/export/export-sql/)
- [Export Templated](/de/reference/workflow-steps/export/export-templated/)
- [Export to Avro](/de/reference/workflow-steps/export/export-to-avro/)
- [Export To CSV](/de/reference/workflow-steps/export/export-to-csv/)
- [Export To Excel](/de/reference/workflow-steps/export/export-to-excel/)
- [Export To Excel Sheets](/de/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export To Google Spreadsheet](/de/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export To HDF](/de/reference/workflow-steps/export/export-to-hdf/)
- [Export To JSON](/de/reference/workflow-steps/export/export-to-json/)
- [Export to ORC](/de/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet](/de/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF](/de/reference/workflow-steps/export/export-to-pdf/)
- [Export To Table Archive](/de/reference/workflow-steps/export/export-to-table-archive/)
- [Export To XML](/de/reference/workflow-steps/export/export-to-xml/)
- [Belege buchen](/de/reference/workflow-steps/export/post-documents/) – eine Tabelle mit Belegen in ein beliebiges eingerichtetes ERP-System buchen
- [Geodatei-Export](/de/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau](/de/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/de/reference/workflow-steps/export/export-hyper/)

## Geschriebene Spalten

Die meisten Export-Schritte schreiben alle Spalten der Quelltabelle in dem Zustand, in dem die Tabelle bei der Ausführung des Schritts vorliegt, und in der Spaltenreihenfolge der Tabelle, wenn der Data Mapper keine Zielspalten aufführt, das heißt, wenn die rechte Tabelle auf der Registerkarte **Spalten** leer ist. Ein nur halb konfigurierter Schritt exportiert daher die gesamte Tabelle an sein Ziel, statt zu scheitern. Prüfen Sie deshalb den Data Mapper, bevor Sie einen Export in ein externes Ziel ausführen.

Sind keine Spalten zugeordnet und hat die Quelltabelle keine, schreibt ein Export von CSV, JSON, SQL, Excel, PDF, Google Spreadsheet oder Kafka nichts und endet mit einer Warnung. Bei einem Export mehrerer Tabellen, etwa XML, Parquet, ORC, Avro oder Excel Sheets, wird diese Tabelle mit einer Warnung, die sie nennt, übersprungen. MongoDB exportieren, Export External Database Tables, Tableau Hyper Export, Geodatei-Export und Run SAP PCM Hyper Loader verhalten sich genauso: Sie sind erfolgreich mit einer Warnung, die die Quelle oder das Ziel nennt, und eine externe Tabelle behält ihre bisherigen Zeilen.
