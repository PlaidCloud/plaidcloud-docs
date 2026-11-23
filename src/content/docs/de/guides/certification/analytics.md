---
title: Lernpfad Analytik
description: Was Sie vor den Praktiker- und Experten-Labs des PlaidCloud-Pfads Analytik lesen sollten und was jedes Lab von Ihnen verlangt.
sidebar:
  label: Analytik
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

Beim Pfad Analytik geht es um Kennzahlen, die unabhängig von ihrer Aufgliederung eine einzige richtige Antwort liefern, und um gemeinsame Bedeutungen über Tabellen hinweg. Beginnen Sie mit dem Lernpfad [Grundlagen](/de/guides/certification/foundations/). Wie Labs funktionieren, lesen Sie unter [PlaidCloud-Zertifizierung](/de/guides/certification/).

## Praktiker

### In dieser Reihenfolge lesen

1. [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/)
2. [Workflow-Protokoll anzeigen](/de/guides/workflows/viewing-workflow-log/)
3. [Kennzahldefinitionen](/de/integrations/ai-coding-agents/metric-definitions/), einschließlich der Ableitung einer Kennzahl aus anderen
4. [Ein Dashboard aus einer veröffentlichten Tabelle erstellen](/de/get-started/tutorials/build-a-dashboard/), für das optionale Dashboard

### Was das Lab verlangt

Das Lab heißt *Analytik: Kennzahlen für drei Fragen definieren*.

Sie führen einen Workflow aus, der eine Verkaufstabelle vorbereitet, und definieren dann auf dieser Tabelle Kennzahlen, jeweils mit Region und Kanal in ihrer Granularität: Umsatz nach Region, durchschnittlicher Bestellwert nach Kanal, abgeleitet aus einer Bestellanzahl, und Kosten als Anteil am Umsatz nach Region, abgeleitet aus einer Kostenkennzahl. Jede Kennzahl baut auf der vorbereiteten Tabelle auf, nicht auf der Rohtabelle. Ein Dashboard für die drei Antworten ist ein guter nächster Schritt, wird aber nicht bewertet.

Das Lab prüft, ob der Workflow läuft und ob jede der drei Kennzahlen die richtige Antwort liefert.

## Experte

Das Experten-Lab ist zeitlich begrenzt: Sie haben ab dem Moment, in dem Sie es starten, 4 Stunden.

### In dieser Reihenfolge lesen

1. [Kennzahldefinitionen](/de/integrations/ai-coding-agents/metric-definitions/)
2. [Datenmodell und Projektelemente](/de/guides/projects/data-model/)
3. [Analysepfade](/de/integrations/ai-coding-agents/analysis-paths/)

### Was das Lab verlangt

Das Lab heißt *Analytik Experte: Kennzahlen, die übereinstimmen*.

Zwei Kennzahlen liefern je nach Aufgliederung unterschiedliche Antworten, und die Umsatzsumme ist größer als die Summe der Bestellungen. Sie reparieren sie so, dass jede nach Region und nach Produkt eine richtige Antwort liefert, und behalten dabei ihre Namen bei. Anschließend machen Sie die Spalten, die dasselbe bedeuten, zu je einem gemeinsamen Element: eines für die Region, über die Tabellen hinweg, die sie unter verschiedenen Spaltennamen führen, und eines für das Produkt.

Das Lab prüft, ob der Workflow läuft, ob der Umsatz nach Region und nach Produkt sowie die Stückzahlen nach Produkt stimmen und ob die Elemente die richtigen Spalten abdecken.
