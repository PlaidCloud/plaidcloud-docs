---
title: Set Project Variable Values from Table-Schritt
description: Liest Werte aus einer Projekttabelle und weist sie Projektvariablen zu, die über Workflow-Ausführungen hinweg erhalten bleiben.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## Beschreibung

Liest Werte aus einer Projekttabelle und weist sie *Projekt*variablen zu. Anders als beim [Set Workflow Variable Values from Table-Schritt](/de/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/) bleiben die Werte über die Ausführung hinaus erhalten – jeder Workflow im Projekt sieht sie, bis sie erneut geändert werden.

Verwenden Sie den Schritt für Zustände, die eine einzelne Ausführung überdauern: die zuletzt erfolgreich geladene Periode, einen Wasserzeichen-Zeitstempel oder den Namen des aktuellen Szenarios.

## Konfiguration

### Quellspalten

Ordnen Sie jede Quellspalte der Projektvariablen zu, die sie füllt. Der Schritt liest eine einzelne Zeile. Schränken Sie die Tabelle daher vor seiner Ausführung auf eine Zeile ein.

### Teilmenge der Daten auswählen

Ein Filterausdruck, der die Quellzeilen einschränkt.

### Sekundären Filter auf Ergebnisdaten anwenden

Ein Filter im Stil von `HAVING`, der nach der Aggregation angewendet wird.

### Final Data Table Slicing (Limit)

Standardmäßig deaktiviert und im aktivierten Zustand auf eine Zeile begrenzt. Aktivieren Sie ihn mit einer expliziten Sortierung, wenn die Quelle mehrere Kandidatenzeilen zurückgeben könnte.

## Verwandte Themen

- [Workflow-Steuerungsschritte](/de/reference/workflow-steps/workflow-control/)
- [Set Project Variable-Schritt](/de/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table-Schritt](/de/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
