---
title: Set Workflow Variable Values from Table-Schritt
description: Liest Werte aus einer Projekttabelle und weist sie Workflow-Variablen zu, sodass spätere Schritte anhand von Daten statt anhand fest codierter Werte verzweigen oder filtern.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## Beschreibung

Liest Werte aus einer Projekttabelle und weist sie Workflow-Variablen zu. Verwenden Sie den Schritt, um einen Workflow durch seine eigenen Daten zu steuern – lesen Sie die zuletzt abgeschlossene Periode, eine Zeilenanzahl oder einen Dateipfad aus einer Steuerungstabelle und lassen Sie nachgelagerte Schritte darauf verweisen.

Die hier gesetzten Variablen gelten für die Dauer der Workflow-Ausführung. Um Werte zu setzen, die über Workflows im Projekt hinweg erhalten bleiben, verwenden Sie den [Set Project Variable Values from Table-Schritt](/de/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Konfiguration

### Quellspalten

Ordnen Sie jede Quellspalte der Workflow-Variablen zu, die sie füllt. Der Schritt liest eine einzelne Zeile. Schränken Sie die Tabelle daher vor seiner Ausführung auf eine Zeile ein.

### Teilmenge der Daten auswählen

Ein Filterausdruck, der die Quellzeilen einschränkt – in der Regel auf die eine Zeile mit den gewünschten Werten.

### Sekundären Filter auf Ergebnisdaten anwenden

Ein Filter im Stil von `HAVING`, der nach der Aggregation angewendet wird, für den Fall, dass der Wert aus einer gruppierten Berechnung stammt.

### Final Data Table Slicing (Limit)

Standardmäßig deaktiviert und im aktivierten Zustand auf eine Zeile begrenzt. Aktivieren Sie ihn mit einer expliziten Sortierung, wenn die Quelle mehrere Kandidatenzeilen zurückgeben könnte und Sie eine bestimmte davon möchten.

## Verwandte Themen

- [Workflow-Steuerungsschritte](/de/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable-Schritt](/de/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table-Schritt](/de/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/)
