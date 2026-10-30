---
title: Standortoptimierer
description: Wählen Sie aus einer Menge von Kandidaten K Standorte, die die gesamte oder gewichtete Entfernung zu einer Menge von Bedarfspunkten minimieren.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

Der Schritt Standortoptimierer wählt aus einer Tabelle mit Kandidatenstandorten **K** Standorte aus, die die gesamte oder gewichtete Entfernung zu einer Tabelle mit Bedarfspunkten minimieren – ein p-Median-Modell zur Standortplanung, das als gemischt-ganzzahliges Programm mit dem HiGHS-Solver von PlaidCloud gelöst wird.

Der Standortoptimierer läuft in einem Workflow-Job-Pod, demselben Job-Image, das auch [Solver](/de/reference/workflow-steps/optimization/solver/) verwendet, und schreibt die Ergebnisse in Projekttabellen zurück.

## Eingaben

### Kandidatenstandorte

Die Tabelle der möglichen Standorte, zugeordnet mit derselben Quell-/Zielspaltenzuordnung, denselben Filtern und derselben Aggregation, die jede tabellenzugeordnete Eingabe verwendet.

### Bedarfspunkte

Die Tabelle der Punkte, deren Entfernung zum nächstgelegenen ausgewählten Standort minimiert wird, auf dieselbe Weise zugeordnet.

### Entfernungstabelle (optional)

Eine vorberechnete Tabelle mit Entfernungen zwischen Kandidaten und Bedarfspunkten. Lassen Sie sie nicht gesetzt, damit der Schritt die Entfernungen selbst berechnet.

### K

Die Anzahl der Standorte, die aus den Kandidatenstandorten ausgewählt werden.

## Solver-Optionen

| Option | Beschreibung |
| --- | --- |
| Zeitlimit | Optionales Laufzeitlimit in Sekunden. |
| MIP-Gap | Optionale relative MIP-Lücke. |
| Presolve aktivieren | Lässt den Solver das Modell vor dem Lösen vereinfachen. Standardmäßig aktiviert. |
| Benutzerdefinierte Ressourcen verwenden | Legt CPU-Kerne und Arbeitsspeicher für den Job-Pod fest. |

Ein Abbruch durch **Zeitlimit** oder **MIP-Gap** liefert die beste innerhalb dieses Limits gefundene Lösung statt des echten Optimums – derselbe Kompromiss, den [Solver](/de/reference/workflow-steps/optimization/solver/#statusverhalten) bei einem nicht optimalen Status eingeht. Lassen Sie beide ungesetzt, um bis zur vollständigen Optimalität zu lösen.

## Ausgaben

Der Standortoptimierer schreibt drei Ausgabetabellen, die alle unterschiedlich benannt sein müssen.

### Ausgabetabelle „Ausgewählte Standorte"

Eine Zeile pro gewähltem Standort.

### Ausgabetabelle „Zuordnung"

Eine Zeile pro Bedarfspunkt, die den ausgewählten Standort nennt, dem er zugeordnet wurde.

### Ausgabetabelle „Zusammenfassung"

Eine Zeile mit Solver-Status, Zielfunktionswert und Ausführungsdetails.

## Grenzen und Einschränkungen

Dieser Schritt ist ein **p-Median**-Modell: Er minimiert stets die gesamte (optional gewichtete) Entfernung von den Bedarfspunkten zu ihrem nächstgelegenen ausgewählten Standort. Er bildet weder einen Score im Gravitationsstil noch eine benutzerdefinierte Bewertungsformel noch ein Ziel ab, bei dem ein höherer Score statt einer geringeren Entfernung besser ist. Ein Standortauswahlproblem, das eines davon benötigt, gehört stattdessen in ein selbst erstelltes [Solver](/de/reference/workflow-steps/optimization/solver/)-Modell.

## Verwandte Themen

- [Solver](/de/reference/workflow-steps/optimization/solver/) – allgemeine lineare und gemischt-ganzzahlige Optimierung, für ein Standortauswahlziel, das das feste p-Median-Modell dieses Schritts nicht abdeckt.
- [Alteryx-Konvertierungsmatrix](/de/reference/alteryx-conversion-matrix/) – das Alteryx-Tool Location Optimizer wird nur für seinen Fall der linearen Entfernungsminimierung in diesen Schritt konvertiert; ein Gravitationskern oder ein benutzerdefiniertes Scoring-Makro wird weiterhin abgelehnt.
