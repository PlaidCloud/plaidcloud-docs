---
title: Lernpfad Data Engineering
description: Was Sie vor den Praktiker- und Experten-Labs des PlaidCloud-Pfads Data Engineering lesen sollten und was jedes Lab von Ihnen verlangt.
sidebar:
  label: Data Engineering
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

Beim Pfad Data Engineering geht es darum, Workflows zu bauen, die korrekt, variablengesteuert und schnell sind. Beginnen Sie mit dem Lernpfad [Grundlagen](/de/guides/certification/foundations/). Wie Labs funktionieren, lesen Sie unter [PlaidCloud-Zertifizierung](/de/guides/certification/).

## Praktiker

### In dieser Reihenfolge lesen

1. [Workflow erstellen](/de/guides/workflows/create-workflow/)
2. [Workflow-Schritte](/de/reference/workflow-steps/), insbesondere die Schritte [Table Inner Join](/de/reference/workflow-steps/tables/table-inner-join/) und [Table Extract](/de/reference/workflow-steps/tables/table-extract/)
3. [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/)
4. [Ihre Arbeit wiederverwenden: Variablen, Makros und UDFs](/de/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/)
6. [Workflow-Protokoll anzeigen](/de/guides/workflows/viewing-workflow-log/)

### Was das Lab verlangt

Das Lab heißt *Datentechnik: monatlicher Umsatzaufbau*.

Drei Rohtabellen sind geladen: Verkaufszeilen, Filialen und Produkte. Im Workflow des Labs bauen Sie eine Monatszusammenfassung mit einer Zeile pro Region und Produktkategorie, mit Stückzahlen und Umsatz, für die verkauften Zeilen eines Monats. Der Monat stammt aus einer Projektvariable, nicht aus einem in einen Schritt eingetippten Wert: Das Lab ändert die Variable und führt den Workflow erneut aus. Verwenden Sie nur Standardschritte, keine SQL- oder Code-Schritte.

Das Lab prüft, ob der Workflow läuft, ob er nur Standardschritte verwendet und ob die Zusammenfassung für den Monat und noch einmal für einen anderen Monat stimmt.

## Experte

Das Experten-Lab ist zeitlich begrenzt: Sie haben ab dem Moment, in dem Sie es starten, 4 Stunden.

### In dieser Reihenfolge lesen

1. [Einen Workflow debuggen](/de/get-started/tutorials/debug-a-workflow/)
2. [Workflow-Protokoll anzeigen](/de/guides/workflows/viewing-workflow-log/)
3. [Schrittfehler verwalten](/de/guides/workflows/managing-step-errors/)
4. [Schrittdaten in der Vorschau anzeigen](/de/guides/workflows/preview-step-data/)
5. [Einen Workflow optimieren](/de/guides/workflows/optimize-a-workflow/)
6. [Workflow-Schritte](/de/reference/workflow-steps/), insbesondere der Schritt [Table Inner Join](/de/reference/workflow-steps/tables/table-inner-join/)

### Was das Lab verlangt

Das Lab heißt *Datentechnik Experte: den nächtlichen Build reparieren und beschleunigen*.

Ein nächtlicher Workflow läuft nicht mehr, und davor war er viel zu langsam. Sie lesen das Ausführungsprotokoll, finden jede Ursache und beheben den Workflow so, dass er erfolgreich läuft, die richtige Zusammenfassung erzeugt und in einem kleinen Bruchteil seiner früheren Zeit fertig wird. Zeilen ohne Konto werden ausgelassen, und doppelt aufgeführte Konten dürfen die Anzahlen nicht aufblähen. Verwenden Sie nur Standardschritte, und lassen Sie die Eingabetabellen unverändert.

Das Lab prüft, ob der Workflow läuft, ob er nur Standardschritte verwendet, ob die Zusammenfassung stimmt, ob die Eingabetabellen unverändert sind und ob der Workflow schnell genug ist.
