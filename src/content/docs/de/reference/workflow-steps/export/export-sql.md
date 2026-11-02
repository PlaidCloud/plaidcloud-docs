---
title: Export to SQL (Schritt)
description: Exportieren Sie Daten aus einem PlaidCloud-Workflow-Schritt in externe SQL-Datenbanken, um Ergebnisse in nachgelagerte Datenbanksysteme zu laden.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Beschreibung



Schreibt eine PlaidCloud-Projekttabelle als SQL-Datei mit CREATE-TABLE- und INSERT-Anweisungen in ein Dokumentenkonto. Nützlich, wenn Sie Daten an ein System übergeben müssen, das SQL-Skripte statt CSV oder Parquet einliest.

Für das direkte Laden in eine entfernte Datenbank verwenden Sie stattdessen den passenden Datenbank-Exportschritt oder [Agent Remote Import](/de/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — diese sind schneller und benötigen keine Zwischendatei.

## Vorschau

**Vorschau** zeigt bis zu 100 Zeilen der Abfrage an, die der Schritt aus der Quelltabelle liest, ohne sie auszuführen. Klicken Sie auf der Registerkarte **Quelle** auf **Vorschau**. Wenn es mehr Zeilen gibt, weist die Vorschau darauf hin, dass sie die ersten Zeilen zeigt und Sie den Schritt ausführen müssen, um alle zu lesen. Die Vorschau setzt Variablen auf dieselbe Weise ein wie eine Ausführung, unterstützt jedoch keine Variablenformate wie `{x:>9}`.

Die Vorschau liest nur Daten. Wenn die Abfrage eine Funktion verwendet, die die Vorschau nicht als schreibgeschützt prüfen kann, zeigt sie *Die Vorschau unterstützt nur Standard-SQL-Funktionen. Führen Sie den Schritt aus, um Ergebnisse zu sehen.* Führen Sie den Schritt aus, um das Ergebnis zu sehen. Die Vorschau ist in einem gesperrten Projekt nicht verfügbar.

## Zusätzliche Einstellungen

In **Zeilenreihenfolge** sortiert **Zeilen sortieren nach** (`sort_columns`) die geschriebenen Zeilen nach diesen Quellspalten, beginnend mit dem ersten Schlüssel, jeweils mit den Einstellungen **Spalte**, **Aufsteigend** und **Nullwerte**. Eine Schlüsselspalte muss nicht geschrieben werden. **Nullwerte** steht standardmäßig bei aufsteigender Sortierung auf zuerst und bei absteigender auf zuletzt. Die Einstellung wird mit **Zusammenfassen** oder **Eindeutig** nicht verwendet.

## Beispiele


Noch keine Beispiele...
