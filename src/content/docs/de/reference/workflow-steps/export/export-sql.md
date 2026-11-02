---
title: Export to SQL
description: Exportieren Sie Daten aus einem PlaidCloud-Workflow-Schritt in externe SQL-Datenbanken, um Ergebnisse in nachgelagerte Datenbanksysteme zu laden.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Beschreibung



Schreibt eine PlaidCloud-Projekttabelle als SQL-Datei mit CREATE-TABLE- und INSERT-Anweisungen in ein Dokumentenkonto. Nützlich, wenn Sie Daten an ein System übergeben müssen, das SQL-Skripte statt CSV oder Parquet einliest.

Zum direkten Laden in eine entfernte Datenbank verwenden Sie stattdessen den passenden Datenbank-Export-Schritt oder [Agent Remote Import](/de/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/). Diese sind schneller und benötigen keine Zwischendatei.

## Vorschau

Die **Vorschau** auf der Registerkarte **Quelle** zeigt bis zu 100 Zeilen der Quelltabelle an, ohne den Schritt auszuführen. Hat die Tabelle mehr Zeilen, weist die Vorschau darauf hin, dass sie nur die ersten Zeilen zeigt. Existiert die Quelltabelle noch nicht, meldet die Vorschau, dass nichts anzuzeigen ist. In einem gesperrten Projekt ist die Vorschau nicht verfügbar.

## Zusätzliche Einstellungen

Unter **Zeilenreihenfolge** sortiert **Zeilen sortieren nach** (`sort_columns`) die geschriebenen Zeilen nach diesen Quellspalten, beginnend mit dem ersten Schlüssel, jeweils mit den Einstellungen **Spalte**, **Aufsteigend** und **Nullwerte**. Eine Schlüsselspalte muss nicht geschrieben werden. **Nullwerte** steht standardmäßig bei aufsteigender Sortierung am Anfang und bei absteigender am Ende. Die Einstellung wird mit **Zusammenfassen** oder **Eindeutig** nicht verwendet.

## Beispiele


Noch keine Beispiele ...
