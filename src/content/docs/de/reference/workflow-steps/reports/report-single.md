---
title: Report Single
description: Erzeugt aus einem PlaidCloud-Workflow-Schritt einen einzelnen PDF-Bericht mithilfe von Vorlagen, Datenquellen und konfigurierbaren Layoutoptionen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## Beschreibung



Rendert einen PDF-Bericht aus einer RML-Vorlage (Report Markup Language), gefüllt mit Daten aus einer oder mehreren PlaidCloud-Tabellen. Verwenden Sie ihn für formelle, formatierte Berichte – Rechnungen, Finanzberichte, behördliche Meldungen, Zusammenfassungen im Corporate Design.

Die RML-Vorlage definiert das Layout (Seitengröße, Schriftarten, fester Text, Platzierung von Tabellen); die Eingabetabellen liefern die variablen Daten. Vergleichen Sie mit [Reports Batch](/de/reference/workflow-steps/reports/reports-batch/), wenn eine Vorlage viele Berichte erzeugen soll (z. B. einen pro Kunde).


## Namen, die die Vorlage liest

Die Vorlage liest jede Quelle auf der Registerkarte **Berichtsdaten** und jede Konstante unter **Berichtskonstanten (feste Werte)** über ihren Namen. Neue Quellen heißen `new_source`, `new_source_2` usw.; die Vorlage kann sie unverändert lesen. Benennen Sie sie um, damit der Name ihren Inhalt beschreibt.


## Was beim Speichern geprüft wird

Jeder Quell- und Konstantenname muss:

- **Angegeben sein** – ein leerer Name wird abgelehnt.
- **Eindeutig sein** – zwei Quellen, zwei Konstanten oder eine Quelle und eine Konstante dürfen keinen gemeinsamen Namen haben, weil die Vorlage nur eine davon sehen würde: *Source name 'sales' is also a constant name; rename one of them.*
- **Von der Vorlage lesbar sein** – Buchstaben, Ziffern und Unterstriche, beginnend mit einem Buchstaben oder Unterstrich: *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **Kein von der Vorlage reserviertes Wort sein** – `True`, `False`, `None`, `true`, `false`, `none`, `not` und `self` werden als etwas anderes als Ihre Daten gelesen: *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Beispiele

Noch keine Beispiele ...
