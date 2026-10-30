---
title: Solver
description: Lösen Sie LP- und MIP-Optimierungsprobleme anhand von Workflow-Tabellendaten.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/solver.md
---

Der Schritt Solver löst Probleme der linearen und der gemischt-ganzzahligen Programmierung anhand von PlaidCloud-Tabellen. Verwenden Sie ihn, wenn ein Workflow Werte wählen muss, die ein Ziel minimieren oder maximieren und dabei lineare Nebenbedingungen erfüllen.

Solver läuft in einem Workflow-Job-Pod und schreibt die Ergebnisse in Projekttabellen zurück.

## Eingaben

Konfigurieren Sie vier Eingabetabellen. Jede Eingabe hat eine Quelltabelle, eine Datenzuordnung und Filter. PlaidCloud übersetzt diese Einstellungen in die Datenbankabfrage, mit der jede Eingabe gelesen wird, sodass die Auswahl erfolgt, bevor Solver die Zeilen erhält.

### Variablen

Eine Zeile pro Entscheidungsvariable.

| Spalte | Beschreibung |
| --- | --- |
| `variable_id` | Eindeutiger Variablenname, den die anderen Eingabetabellen verwenden. |
| `lower_bound` | Minimalwert. Lassen Sie das Feld leer für keine Untergrenze. |
| `upper_bound` | Maximalwert. Lassen Sie das Feld leer für keine Obergrenze. |
| `type` | `continuous`, `integer` oder `binary`. Binäre Variablen verwenden die Grenzen `0` und `1`. |

### Zielfunktion

Eine Zeile pro Variable mit einem Zielfunktionskoeffizienten ungleich null.

| Spalte | Beschreibung |
| --- | --- |
| `variable_id` | Variable aus der Eingabe „Variablen". |
| `coefficient` | Zielfunktionskoeffizient dieser Variable. |

Variablen, die in dieser Tabelle fehlen, verwenden den Koeffizienten `0`.

### Nebenbedingungen

Eine Zeile pro linearer Nebenbedingung.

| Spalte | Beschreibung |
| --- | --- |
| `constraint_id` | Eindeutiger Name der Nebenbedingung, den die Eingabe „Koeffizienten" verwendet. |
| `lower_bound` | Minimal zulässige Aktivität. Lassen Sie das Feld leer für keine Untergrenze. |
| `upper_bound` | Maximal zulässige Aktivität. Lassen Sie das Feld leer für keine Obergrenze. |

Legen Sie für eine Gleichheitsnebenbedingung dieselbe Unter- und Obergrenze fest.

### Koeffizienten

Dünnbesetzte Matrix der Koeffizienten der Nebenbedingungen.

| Spalte | Beschreibung |
| --- | --- |
| `constraint_id` | Nebenbedingung aus der Eingabe „Nebenbedingungen". |
| `variable_id` | Variable aus der Eingabe „Variablen". |
| `coefficient` | Koeffizient dieser Variable in dieser Nebenbedingung. |

## Solver-Optionen

| Option | Beschreibung |
| --- | --- |
| Optimierungsrichtung | Wählen Sie Minimieren oder Maximieren. |
| Zeitlimit | Optionales Laufzeitlimit in Sekunden. |
| MIP-Gap | Optionale relative MIP-Lücke für gemischt-ganzzahlige Probleme. |
| Presolve aktivieren | Lässt den Solver das Modell vor dem Lösen vereinfachen. |
| Benutzerdefinierte Ressourcen verwenden | Legt CPU-Kerne und Arbeitsspeicher für den Job-Pod fest. |

## Ausgaben

Solver schreibt drei Ausgabetabellen.

### Lösungstabelle

Enthält eine Zeile pro Variable mit dem gelösten Wert, den Grenzen, dem Variablentyp, dem Zielfunktionskoeffizienten und, sofern verfügbar, den reduzierten Kosten.

### Nebenbedingungs-Ergebnistabelle

Enthält eine Zeile pro Nebenbedingung mit Aktivität, Grenzen, Schlupf und, sofern verfügbar, dem Dualwert.

### Zusammenfassungstabelle

Enthält eine Zeile mit Solver-Status, Zielfunktionswert, Laufzeit, MIP-Lücke, dualer MIP-Schranke, Knotenanzahl, Iterationsanzahl, Variablenanzahl und Anzahl der Nebenbedingungen.

## Statusverhalten

Eine optimale Lösung schließt den Schritt erfolgreich ab. Liefert der Solver eine verwendbare Lösung mit nicht optimalem Status, endet der Schritt mit einer Warnung und schreibt die Ausgabetabellen trotzdem. Ist keine verwendbare Lösung verfügbar, schlägt der Schritt mit der Statusmeldung des Solvers fehl.
