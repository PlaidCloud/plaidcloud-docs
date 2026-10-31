---
title: Schnellstart für Umlagen
description: Richten Sie mit dieser Schritt-für-Schritt-Anleitung zu Quellen, Treibern und Zielzuordnung schnell eine einfache Kostenumlage in PlaidCloud ein.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

Diese Anleitung führt Sie in etwa 30 Minuten von den Rohdaten der Kosten zu einem funktionierenden Umlagemodell.

## Was Sie benötigen

- Ein Projekt mit mindestens zwei Tabellen:
  - **Umzulegende Werte** — die Kosten (oder Erlöse oder Mengen), die Sie verteilen möchten. Eine Zeile pro Quelleinheit, eine Spalte mit dem Betrag.
  - **Treiberdaten** — die Grundlage für die Verteilung. Mitarbeiterzahl, Fläche in Quadratmetern, Anzahl der Transaktionen, Umsatz — wonach auch immer Sie umlegen möchten.
- Eine Dimension, die Quelle und Ziel verbindet (Kostenstellen, Abteilungen, Produkte — je nachdem, welche Taxonomie zu Ihrem Modell passt).

Wenn Sie noch nicht alles beisammen haben, erfahren Sie in den Anleitungen [Tabellen und Ansichten](/de/guides/data/) und [Dimensionen](/de/guides/dimensions/), wie Sie die Eingabedaten laden.

## Schritte

1. **Öffnen Sie das Projekt**, das Ihre Werte- und Treibertabellen enthält.
2. **Erstellen Sie einen neuen Workflow.** Umlagen werden immer innerhalb eines Workflows ausgeführt — sie arbeiten nicht direkt auf Tabellen außerhalb eines Workflows.
3. **Fügen Sie einen Umlageschritt hinzu.** Fügen Sie im Workflow einen Schritt aus der Kategorie **Allocation** hinzu. Der gängigste Ausgangspunkt ist **Allocation Rules** für eine einfache, treiberbasierte Verteilung.
4. **Konfigurieren Sie die Quelle.** Verweisen Sie den Schritt auf Ihre Werttabelle und wählen Sie die Spalte mit dem umzulegenden Betrag.
5. **Konfigurieren Sie den Treiber.** Verweisen Sie den Schritt auf die Treibertabelle und wählen Sie die Spalte mit den Treiberwerten.
6. **Ordnen Sie die Dimension zu.** Legen Sie fest, welche Spalte in jeder Tabelle die Dimensionsmitglieder enthält. Der Umlageschritt gleicht anhand dieser Spalten Quellzeilen mit Treiberzeilen ab.
7. **Führen Sie den Schritt aus.** Das Ergebnis ist eine neue Tabelle mit einer Zeile pro verteiltem Betrag.
8. **Prüfen Sie die Ergebnisse.** Kontrollieren Sie, ob die Summen Ihren Erwartungen entsprechen — die Summe der umgelegten Beträge sollte der Summe der Quellbeträge entsprechen (im Rahmen der Rundungstoleranz).

## Häufige weiterführende Aufgaben

- **Rekursiv verteilen** — wenn ein Ziel selbst Treiber für eine weitere Umlage enthält, lesen Sie [Rekursive Umlagen](/de/guides/allocations/setup/recursive-allocations/).
- **Zeilen für die Umlage markieren** — wie Sie steuern, *welche* Zeilen auf welche Ziele umgelegt werden, lesen Sie unter [Regelbasiertes Tagging](/de/guides/allocations/getting-started/rule-based-tagging/).
- **Unerwartete Ergebnisse untersuchen** — wenn Summen nicht abstimmen oder einzelne Zeilen falsch aussehen, lesen Sie [Fehlerbehebung bei Umlagen](/de/guides/allocations/results/troubleshooting-allocations/).

## Nächste Schritte

- [Wozu sind Umlagen nützlich?](/de/guides/allocations/getting-started/why-are-allocations-useful/) — wann Sie sie einsetzen
- [Eine Umlage konfigurieren](/de/guides/allocations/setup/configure-an-allocation/) — ausführliche Konfigurationsreferenz
- [Schritttypen für Umlagen](/de/reference/workflow-steps/allocation/) — alle Workflow-Schritte der Kategorie Allocation
