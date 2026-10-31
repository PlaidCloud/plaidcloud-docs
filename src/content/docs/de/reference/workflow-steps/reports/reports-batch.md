---
title: Reports Batch
description: Erzeugt aus einem PlaidCloud-Workflow-Schritt PDF-Berichte im Stapel, um mehrere Berichte aus Vorlagen mit unterschiedlichen Dateneingaben zu erstellen.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## Beschreibung



Rendert viele PDF-Berichte aus einer einzigen RML-Vorlage, gesteuert durch eine Steuertabelle. Pro Zeile der Steuertabelle wird ein Bericht erzeugt, wobei die Spaltenwerte der jeweiligen Zeile als Parameter für das Rendering dieses Berichts dienen.

Typische Verwendung: Kundenkontoauszüge (ein PDF pro Kunde), Finanzberichte pro Einheit (ein PDF pro Geschäftseinheit), Rechnungen (ein PDF pro Auftrag). Vergleichen Sie mit [Report Single](/de/reference/workflow-steps/reports/report-single/) für die einmalige Berichtserstellung.


## Namen, die die Vorlage liest

Die Vorlage liest jede Quelle auf der Registerkarte **Berichtsdaten** und jede Zielspalte der Zuordnung **Datenquelle der Stapeldatensatzwerte** über ihren Namen. Es gibt keinen Abschnitt für Konstanten: Jede Stapelzeile liefert die Werte der Vorlage für ihren Bericht. Neue Quellen heißen `new_source`, `new_source_2` usw.; die Vorlage kann sie unverändert lesen.


## Was beim Speichern geprüft wird

Jeder Quell- und Stapelspaltenname muss angegeben, eindeutig und von der Vorlage lesbar sein – dieselben Regeln wie bei [Report Single](/de/reference/workflow-steps/reports/report-single/), mit Stapelspalten anstelle von Konstanten: *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Wird gespeichert, obwohl eine Stapelquelltabelle gewählt, die Stapelzuordnung aber leer ist, füllt der Schritt die Zuordnung aus dieser Tabelle, so wie es Populate täte.


## Leere Stapeltabelle

Hat die Stapelquelltabelle keine Zeilen, wird der Schritt erfolgreich mit einer Warnung beendet, die die Stapeltabelle nennt, und es werden keine Berichte erzeugt.


## Beispiele

Noch keine Beispiele ...
