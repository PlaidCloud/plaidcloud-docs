---
title: Export to SQL
description: Exportieren Sie Daten aus einem PlaidCloud-Workflow-Schritt in externe SQL-Datenbanken, um Ergebnisse in nachgelagerte Datenbanksysteme zu laden.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Beschreibung



Schreibt eine PlaidCloud-Projekttabelle als SQL-Datei mit CREATE-TABLE- und INSERT-Anweisungen in ein Dokumentenkonto. Nützlich, wenn Sie Daten an ein System übergeben müssen, das SQL-Skripte statt CSV oder Parquet einliest.

Zum direkten Laden in eine Remote-Datenbank verwenden Sie stattdessen den passenden Datenbank-Exportschritt oder [Agent Remote Import](/de/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) – diese sind schneller und benötigen keine Zwischendatei.

## Zusätzliche Einstellungen

Unter **Zeilenreihenfolge** sortiert **Zeilen sortieren nach** (`sort_columns`) die geschriebenen Zeilen nach diesen Quellspalten, zuerst der erste Schlüssel, jeweils mit den Einstellungen **Spalte**, **Aufsteigend** und **Nullwerte**. Eine Schlüsselspalte muss nicht geschrieben werden. **Nullwerte** steht bei aufsteigender Sortierung standardmäßig am Anfang und bei absteigender am Ende. Die Option wird nicht zusammen mit **Zusammenfassen** oder **Eindeutig** verwendet.

## Beispiele


Noch keine Beispiele ...
