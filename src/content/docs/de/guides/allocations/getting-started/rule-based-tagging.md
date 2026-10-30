---
title: Regelbasiertes Tagging
description: Konfigurieren Sie regelbasiertes Tagging in PlaidCloud-Umlagen, um Datensätze anhand definierter Kriterien automatisch zu kategorisieren und zu kennzeichnen.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

Mit regelbasiertem Tagging versehen Sie Quellzeilen mit Metadaten, anhand derer die Umlage-Engine entscheidet, *wohin* diese Zeilen gehen. Nutzen Sie es, wenn sich das Umlageverhalten je Zeile unterscheiden soll — etwa wenn die Kosten einer Kostenstelle nach Mitarbeiterzahl, die einer anderen aber nach Umsatz verteilt werden sollen.

## Wann Sie es einsetzen

- Eine pauschale Umlageregel bildet nicht ab, wie die Kosten tatsächlich verteilt werden sollen (unterschiedliche Regeln für unterschiedliche Kostenarten).
- Sie möchten bestimmte Quellzeilen gezielt auf bestimmte Ziele lenken und die übrigen normal verteilen lassen.
- Sie bilden eine Umlage mit mehreren Pools ab, bei der jeder Pool einen anderen Treiber verwendet.

## So funktioniert Tagging

1. **Quelle taggen.** Die Werttabelle erhält eine oder mehrere Tag-Spalten, die jede Zeile klassifizieren.
2. **Tags in der Umlageregel verwenden.** Beim Konfigurieren des Umlageschritts formulieren Sie Regeln in der Form *„Wenn Quell-Tag X = Wert Y, dann mit Treiber D und Zieldimension T umlegen.“*
3. **Die Engine leitet die Zeilen weiter.** Jede Quellzeile wird der Reihe nach mit den Regeln abgeglichen; die erste passende Regel bestimmt das Umlageverhalten.

## Quellmuster, die sich für Tagging eignen

- Eine Spalte `cost_category` mit Werten wie `payroll`, `facilities`, `it`, `marketing`
- Eine Spalte `pool`, die den Umlagepool benennt, zu dem die Zeile gehört
- Eine boolesche Spalte wie `is_overhead`, die eine abweichende Behandlung auslöst

## Beispiel

Eine Kostentabelle mit `cost_center` und `cost_category`:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

Sie können zwei Umlageregeln konfigurieren:

- **Payroll-Zeilen** werden über den Treiber Mitarbeiterzahl verteilt
- **IT-Zeilen** werden über den Treiber Benutzeranzahl verteilt

Beide Regeln laufen auf derselben Quelltabelle; die Tags entscheiden, welche Regel für welche Zeile gilt.

## Verwandte Themen

- [Schnellstart für Umlagen](/de/guides/allocations/getting-started/allocations-quick-start/) — der grundlegende Ablauf, bevor Sie Tagging hinzufügen
- [Eine Umlage konfigurieren](/de/guides/allocations/setup/configure-an-allocation/) — vollständige Schrittreferenz
- [Schritt „Allocation Rules“](/de/reference/workflow-steps/allocation/allocation-rules/) — der Workflow-Schritt, der getaggte Daten verarbeitet
