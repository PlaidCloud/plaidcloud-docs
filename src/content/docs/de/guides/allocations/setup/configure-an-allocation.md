---
title: Umlage konfigurieren
description: Konfigurieren Sie eine PlaidCloud-Umlage mit Quelldaten, Treiberdaten, Zielzuordnung, Umlagemethoden und Verarbeitungsoptionen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/configure-an-allocation.md
---

## Zweck

Umlagen ermöglichen es, Werte (typischerweise Kosten) mithilfe eines Treibers auf eine feinere Ebene herunterzubrechen. Umlagen dienen vielfältigen Zwecken, darunter **Activity-Based Costing**, **IT- und Shared-Service-Verrechnung**, die Berechnung der vollen Kosten für die Herstellung und Bereitstellung eines Guts oder einer Dienstleistung für Kunden und vieles mehr. Sie sind ein grundlegendes Werkzeug der Finanzanalyse und ein Eckpfeiler für Management-Reporting wie **Kunden- und Produktrentabilität**. Sie eignen sich außerdem zum Festlegen und Verwalten globaler konzerninterner Verrechnungspreise für Güter und Dienstleistungen.

## Den Umlage-Transform einrichten

Praktisch werden Umlagen in PlaidCloud ähnlich wie andere Daten-Transforms, etwa Joins und Lookups, eingerichtet. Vier Konfigurationsparameter müssen gesetzt sein, damit ein Umlage-Transform erfolgreich ist.

1. **Vorab umgelegte Daten angeben**: Geben Sie die Tabelle mit den Daten vor der Umlage im Abschnitt **Tabelle der zu verteilenden Werte** des Umlage-Transforms an.
2. **Treiberdaten angeben**: Die Treiberdaten bilden die Grundlage für die Verhältnisse, die bei der Umlage verwendet werden. Wählen Sie die Treiberdatentabelle im Abschnitt **Treiberdatentabelle** des Umlage-Transforms.
3. **Ergebnistabelle angeben**: Die Daten nach der Umlage müssen in einer Tabelle gespeichert werden. Geben Sie die Tabelle im Abschnitt **Umlageergebnistabelle** des Ergebnisbereichs des Transforms an.
4. **Zuweisungsdimension angeben**: Umlagen erfordern eine Zuweisungsdimension, die vorgibt, wie jeder Datensatz oder jede Gruppe von Datensätzen der Daten vor der Umlage zugewiesen wird. Geben Sie die Zuweisungsdimension im Abschnitt **Zuweisungsdimensionshierarchie** des Umlage-Transforms an.

Über diese vier hinaus müssen auf den beiden Zuordnungs-Registerkarten die **Rollen** der Spalten festgelegt sein, bevor der Schritt gespeichert wird: eine Spalte **Umzulegender Wert** in der **Umlagequellzuordnung** sowie die Spalten **Wert aufteilen**, **Quellbezug (Nenner)** und **Umlageziel (Zähler)** in der **Treiberdatenzuordnung**. PlaidCloud prüft dies beim Speichern und nennt, was fehlt — siehe [Umlagen beheben](/de/guides/allocations/results/troubleshooting-allocations/#warum-ein-umlageschritt-nicht-gespeichert-wird).

## Grundlegende Konzepte

Die Summe der Werte in einem umgelegten Datensatz sollte mit denen der Quelldaten vor der Umlage übereinstimmen.

Umlagen sind in PlaidCloud als Transform-Option verfügbar. Um eine Umlage einzurichten, richten Sie zuerst Zuweisungen ein und konfigurieren Sie dann einen Umlage-Transform, der die Zuweisungen verwendet, um eingehende Datensätze mithilfe einer angegebenen Treibertabelle umzulegen.

Zuweisungen sind besondere Dimensionen. Sie sind im Bereich „Dimensionen“ eines PlaidCloud-Projekts zugänglich.

Um eine Zuweisungsdimension einzurichten, gehen Sie wie folgt vor:

1. Navigieren Sie vom Projektbildschirm aus zur Registerkarte „Dimensionen“.
2. Erstellen Sie eine neue Dimension.
