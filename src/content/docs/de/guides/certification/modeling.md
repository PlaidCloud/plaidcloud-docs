---
title: Lernpfad Modellierung
description: Was Sie vor den Praktiker- und Experten-Labs des PlaidCloud-Pfads Modellierung lesen sollten und was jedes Lab von Ihnen verlangt.
sidebar:
  label: Modellierung
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

Beim Pfad Modellierung geht es um Dimensionen und Umlagen: Hierarchien aufbauen, Kosten nach Treibern verteilen und nachweisen, dass die Ergebnisse aufgehen. Beginnen Sie mit dem Lernpfad [Grundlagen](/de/guides/certification/foundations/). Wie Labs funktionieren, lesen Sie unter [PlaidCloud-Zertifizierung](/de/guides/certification/).

## Praktiker

### In dieser Reihenfolge lesen

1. [Erste Schritte mit Dimensionen](/de/guides/dimensions/getting-started/)
2. [Hierarchien verwalten](/de/guides/projects/managing-hierarchies/)
3. [Eine Dimensionshierarchie entwerfen](/de/get-started/tutorials/design-a-dimension/)
4. [Schnellstart für Umlagen](/de/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split](/de/reference/workflow-steps/allocation/allocation-split/)
6. [Ein Umlagemodell erstellen](/de/get-started/tutorials/build-an-allocation/)
7. [Umlageergebnisse](/de/guides/allocations/results/allocation-results/)
8. [Workflow-Protokoll anzeigen](/de/guides/workflows/viewing-workflow-log/)

### Was das Lab verlangt

Das Lab heißt *Modellierung: gemeinsame IT-Kosten zuordnen*.

Eine Tabelle listet jede Abteilung mit ihrer übergeordneten Abteilung auf. Sie bauen eine Dimension, deren Haupthierarchie genau diesem Baum entspricht. Anschließend verteilen Sie im Workflow des Labs einen Kostenpool im Verhältnis zur Mitarbeiterzahl auf die Abteilungen, mit einer Ergebniszeile pro Abteilung. Eine zweite Treibertabelle ist ebenfalls vorhanden, und sie ist nicht der Treiber für diesen Pool.

Das Lab prüft, ob der Workflow läuft, ob die Hierarchie stimmt, ob die umgelegte Summe mit der Quelle übereinstimmt und ob jede Abteilung den richtigen Betrag erhält.

## Experte

Das Experten-Lab ist zeitlich begrenzt: Sie haben ab dem Moment, in dem Sie es starten, 4 Stunden.

### In dieser Reihenfolge lesen

1. [Eine Umlage konfigurieren](/de/guides/allocations/setup/configure-an-allocation/)
2. [Fehlerbehebung bei Umlagen](/de/guides/allocations/results/troubleshooting-allocations/)
3. [Umlagen mit einem MCP-verbundenen KI-Agenten nachverfolgen](/de/integrations/ai-coding-agents/tracing-allocations/)
4. [Umlageergebnisse](/de/guides/allocations/results/allocation-results/)
5. [Ein Treiber-Was-wäre-wenn ausprobieren](/de/guides/allocations/results/driver-what-if/)
6. [Hierarchien verwalten](/de/guides/projects/managing-hierarchies/)

### Was das Lab verlangt

Das Lab heißt *Modellierung Experte: das Zuordnungsmodell reparieren*.

Ein zweistufiges Umlagemodell geht nicht mehr mit dem Hauptbuch auf, und einige Abteilungen sind offensichtlich falsch. Sie verfolgen die Ursache und beheben das Modell: Jede Stufe verteilt genau ihren Pool, die Abteilungssummen stimmen und ergeben zusammen das Hauptbuch, und die Abteilungsdimension enthält nur die Abteilungen, die es gibt. Es darf keine Ausgleichszeile verwendet werden, um etwas zum Aufgehen zu bringen. Anschließend fügen Sie einen Schritt hinzu, der zeigt, was die IT jede Abteilung kosten würde, wenn sie nach Fläche statt nach Mitarbeiterzahl umgelegt würde.

Das Lab prüft, ob der Workflow läuft, ob die Hierarchie stimmt, ob jede Stufe und die Abteilungssummen mit dem Hauptbuch übereinstimmen, ob jede Abteilung die richtige Summe erhält und ob das Szenario mit der Fläche stimmt.
