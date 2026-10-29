---
title: Dimension Export
description: Exportiert Dimensionsdaten aus PlaidCloud in einem Workflow-Schritt, um hierarchische Strukturen als Dateien zu speichern oder an andere Systeme zu übertragen.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## Beschreibung

Verflacht eine Dimension in eine tabellarische PlaidCloud-Tabelle – eine Zeile pro Mitglied mit Spalten für übergeordnetes Element, Ebene, Wert, Aliasnamen und Eigenschaften. Verwenden Sie dies, wenn Sie die Dimensionsstruktur abfragen, verknüpfen oder an nachgelagerte Systeme weitergeben müssen, die das hierarchische Format von PlaidCloud nicht direkt lesen können.

Typische Verwendung: Exportieren Sie die Dimension als Tabelle und schreiben Sie sie dann mit einem regulären Exportschritt in ein externes System (BI-Tool, Berichtsdatenbank, Dateiübergabe).

## Jede Hierarchie exportieren

Wählen Sie **Alle Hierarchien**, um jede Hierarchie in eine einzige Tabelle zu übernehmen. Das Ergebnis erhält eine Spalte `hierarchy`, die angibt, zu welcher Hierarchie die jeweilige Zeile gehört; die Zeilen sind so geordnet, dass die Haupthierarchie zuerst steht, gefolgt von den Alternativen in alphabetischer Reihenfolge.
