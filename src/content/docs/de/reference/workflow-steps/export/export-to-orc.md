---
title: Export to ORC
description: Exportieren Sie PlaidCloud-Projekttabellen als Apache-ORC-Dateien in ein Dokumentenkonto, spaltenorientiert und mit dem von Ihnen gewählten Komprimierungscodec.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## Beschreibung

Schreibt Projekttabellen als [Apache-ORC](https://orc.apache.org/)-Dateien in ein Dokumentenkonto, eine Datei pro Tabelle. ORC ist ein spaltenorientiertes Format, das von Hive, Spark und den meisten Cloud-Datenplattformen gelesen wird und das Schema in der Datei mitführt. Kombinieren Sie es mit [Import ORC](/de/reference/workflow-steps/import/import-orc/).

Das Schrittformular hat eine Seite **Dateiparameter** für die Zieldatei, das Präfix, die Komprimierung und das Verhalten, wenn die Datei existiert, sowie eine Seite **Datensatzparameter**, die die zu exportierenden Tabellen mit jeweils eigener Tabellendatenauswahl und eigenen Datenfiltern auflistet. [Migrierte KNIME-Workflows](/de/guides/workflows/migrate-knime-workflows/) verwenden diesen Schritt für ORC-Writer.

## Konfiguration

* **Zieldatei** (`output_file`) — das Dokumentenkonto und der Ordner, in die die Dateien geschrieben werden.
* **Präfix der Zieldatei** (`file_name`) — das Dateipräfix. Jede Tabelle wird als `<prefix><table name>.orc` geschrieben.
* **Komprimierungsoption** (`compression`) — der ORC-Codec, der innerhalb der Datei verwendet wird: **Snappy**, **zlib**, **gzip** (wird als `zlib` geschrieben), **Zstandard** oder **LZ4**. Mit **Keine** wird die Datei unkomprimiert geschrieben.
* **Datensatzparameter** (`frames`) — die zu exportierenden Tabellen. Jeder Frame enthält seine eigenen Tabelleneinstellungen. Eine Einstellung auf Tabellenebene, die oben im Schritt statt innerhalb eines Frames steht, wird nicht gelesen.
  * `id` — die Bezeichnung der Tabelle in Warnungen.
  * `source` — die zu exportierende Projekttabelle. Jede Datei wird danach benannt.
  * `source_columns` und `target_columns` — die gelesenen und die geschriebenen Spalten, mit eventueller Umbenennung, Typ und Aggregation pro Spalte.
  * `source_where` — ein Filter auf die Quellzeilen.
  * `aggregate` und `aggregation_type` — fasst die Zeilen zusammen. `aggregation_type` ist die Zusammenfassung, die auf Spalten angewendet wird, die keine eigene festlegen.
  * `having` — ein Filter auf die zusammengefassten Zeilen.
  * `distinct` — schreibt nur eindeutige Zeilen.
  * `use_target_slicer`, `limit_target_start` und `limit_target_end` — schreibt nur die Zeilen von der Startposition bis zur Endposition des Ergebnisses.
  * `sort_columns` — wird mit einem KI-Assistenten oder der REST-API festgelegt, um die geschriebenen Zeilen nach diesen Quellspalten zu sortieren, beginnend mit dem ersten Schlüssel, jeweils `{source, ascending, nulls}`. Eine Schlüsselspalte muss nicht geschrieben werden. `nulls` steht bei aufsteigender Sortierung standardmäßig auf `first` und bei absteigender auf `last`. Wird nicht zusammen mit `aggregate` oder `distinct` verwendet.
* **Eine bereits vorhandene Datei** (`if_exists`), unter **Wenn die Datei existiert** — **Überschreiben** (`overwrite`, Standard) ersetzt eine bereits vorhandene Datei. **Den Schritt fehlschlagen lassen, ohne etwas zu schreiben** (`fail`) beendet den Schritt, ohne etwas zu schreiben, wenn eine Datei, die er schreiben würde, bereits existiert.

## Verwandte Themen

- [Export-Schritte](/de/reference/workflow-steps/export/)
- [Import ORC](/de/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/de/reference/workflow-steps/export/export-to-parquet/)
