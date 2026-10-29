---
title: Umlagen beheben
description: Beheben Sie Probleme mit PlaidCloud-Umlagen, einschließlich häufiger Fehler, Konfigurationsproblemen und Techniken zur Fehlersuche in Ergebnissen.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## Warum ein Umlageschritt nicht gespeichert wird

PlaidCloud prüft die Spaltenzuordnung eines Umlageschritts beim Speichern. Eine Zuordnung, die nicht ausgeführt werden kann, wird an dieser Stelle abgelehnt, und zwar mit einer Benachrichtigung **Speichern nicht möglich**, die auflistet, was zu beheben ist; das Formular wechselt zu der Registerkarte, die das Problem enthält. Früher wurde ein solcher Schritt ohne Beanstandung gespeichert und stoppte den Workflow dann mitten in einer Ausführung — oft erst nach Minuten und mit einer Meldung, die eine Anzahl statt eines Felds nannte.

Geprüft wird erst, wenn Sie sowohl die **Tabelle der zu verteilenden Werte** als auch die **Treiberdatentabelle** gewählt haben. Die Spaltenzuordnung wird aus diesen beiden Tabellen aufgebaut; solange nicht beide festgelegt sind, fragt der Schritt nur nach den Tabellen selbst.

### Umlagequellzuordnung

**"No columns specified for allocation."**
Legen Sie die **Rolle** von mindestens einer Spalte auf **Umzulegender Wert** fest. Diese Spalte enthält die Werte, die auf die Ziele verteilt werden.

**"Only numeric columns can be allocated, but ... is not numeric."**
Eine als **Umzulegender Wert** markierte Spalte hat einen nicht numerischen **Typ**. Ändern Sie den Typ in einen numerischen — Numeric, Currency, Integer, Big Integer, Small Integer, Tiny Integer, Float, Double, Decimal, Serial oder Big Serial.

**"Rename the `alloc_status` target column."**
Eine Umlage schreibt eine eigene Spalte `alloc_status` in die Ergebnistabelle, daher kollidiert eine Zielspalte mit diesem Namen damit. Benennen Sie Ihre Spalte um.

### Treiberdatenzuordnung

**"No driver split value column found."**
Legen Sie die **Rolle** einer Treiberspalte auf **Wert aufteilen** fest. Diese Spalte enthält die Gewichte oder Prozentsätze, durch die die Umlage teilt.

**"The driver value column ... must be numeric."**
Ändern Sie den **Typ** der Spalte **Wert aufteilen** in einen numerischen.

**"No driver relation columns specified."**
Legen Sie die **Rolle** von mindestens einer Treiberspalte auf **Quellbezug (Nenner)** fest. Dadurch werden die Treiberzeilen den Quellzeilen zugeordnet.

**"No allocation target columns are indicated."**
Legen Sie die **Rolle** von mindestens einer Treiberspalte auf **Umlageziel (Zähler)** fest. Diese werden zu den Zielen der Umlage und erscheinen in der Ergebnistabelle.

**"Driver relation columns do not exist in the source data."**
Zu einer als **Quellbezug (Nenner)** markierten Spalte gibt es in der **Umlagequellzuordnung** keine Spalte mit demselben Namen. Benennen Sie sie entsprechend um oder fügen Sie die Spalte zur Quellzuordnung hinzu.

**"Allocation value column ... is also used as a numerator or denominator column."**
Derselbe Spaltenname ist in der Quellzuordnung ein **Umzulegender Wert** und in der Treiberzuordnung ein **Quellbezug (Nenner)** oder ein **Umlageziel (Zähler)**. Benennen Sie eine der beiden um, damit sich der umzulegende Wert von den Spalten unterscheidet, die beschreiben, wohin er geht.

### Nur Aufteilung mit Dimension

**"Please select a hierarchy to use for the allocation dimension."**
Wählen Sie auf der Registerkarte **Datentabelleneinstellungen** eine **Zuweisungsdimensionshierarchie**. Siehe [Umlage konfigurieren](/de/guides/allocations/setup/configure-an-allocation/).

## Gestrandete Kosten


Gestrandete Kosten sind....



## Überumlage von Kosten


Eine Überumlage von Kosten liegt vor, wenn am Ende mehr Ausgabekosten entstehen...



## Fehlerhafte Umlage von Kosten


Eine fehlerhafte Umlage von Kosten entsteht, wenn...
