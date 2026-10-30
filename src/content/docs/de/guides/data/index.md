---
title: Datenverwaltung – tabellarisch
description: Verwalten Sie tabellarische Daten in PlaidCloud mit Tabellen, Ansichten und der leistungsstarken Lakehouse-Engine für Datenverarbeitung in jeder Größenordnung.
sidebar:
  label: Übersicht
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

Die Datenschicht von PlaidCloud baut auf **Tabellen** (strukturierte Daten in Zeilen und Spalten) und **Ansichten** (gespeicherte Abfragen über Tabellen) auf. Beide liegen in einem Projekt und werden von der Lakehouse-Engine betrieben, die von kleinen Referenztabellen bis zu analytischen Datensätzen mit Milliarden Zeilen skaliert – ohne Konfigurationsänderungen.

## Inhalt dieses Abschnitts

- [Tabellen und Ansichten](/de/guides/data/tables-views/) – was beides ist, wann Sie welches verwenden und wie sie zusammenwirken
- [Tabellen-Explorer](/de/guides/data/table-explorer/) – Tabellen in Ihrem Projekt durchsuchen und prüfen
- [Datentyp Currency](/de/guides/data/currency-data-type/) – ein exakter Spaltentyp mit halber Breite für Geldwerte und wann Sie ihn gegenüber Numeric wählen
- [Datentyp Vector](/de/guides/data/vector-data-type/) – vorberechnete Embeddings in einer Projekttabelle speichern, die erwartete Breite deklarieren und nach den nächstgelegenen Zeilen suchen
- [Tabellen-Snapshots](/de/guides/data/table-snapshots/) – den Snapshot-Verlauf durchsuchen, Daten zum Stand eines früheren Snapshots anzeigen und eine Tabelle zurücksetzen oder wiederherstellen
- [Daten veröffentlichen](/de/guides/data/publish/) – Projekttabellen für Dashboards, BI-Werkzeuge und nachgelagerte Systeme bereitstellen und deren Leistungshinweise prüfen
- [Den neuesten Datensatz in einer großen Verlaufstabelle auswählen](/de/guides/data/selecting-latest-record-in-large-history-table/) – ein verbreitetes Muster mit einer leistungsbewussten Lösung
- [Geocoding API](/de/guides/data/geocoding-api/) – eine Google- oder Mapbox-Geokodierungsintegration auf die REST-Geokodierungs-Endpunkte von PlaidCloud migrieren
- [Drive-Time-Routing-API](/de/guides/data/drive-time-routing-api/) – Opt-in-Vorschau: Fahrzeit-Isochronen und Rangfolge nach nächster Fahrzeit über REST

## Woher die Daten stammen

Tabellen werden typischerweise von **Workflows** befüllt – automatisierten Pipelines, die Daten importieren, transformieren und die Ergebnisse zurückschreiben. Wie Sie sie aufbauen, lesen Sie unter [Workflows](/de/guides/workflows/); jeden verfügbaren Schritttyp finden Sie in der [Referenz der Workflow-Schritte](/de/reference/workflow-steps/).

Informationen zum Anbinden externer Systeme als Datenquellen finden Sie unter [Verbindungen (Leitfaden)](/de/guides/connections/) und [Konnektoren (Referenz)](/de/reference/connectors/).

## Verwandte Themen

- [Konzepte](/de/get-started/concepts/) – wie Tabellen mit Workflows, Dimensionen und dem übrigen Datenmodell zusammenhängen
- [Projekte](/de/guides/projects/) – Projekte besitzen die Tabellen; Tabellen existieren nicht außerhalb eines Projekts
- [Dashboards](/de/guides/dashboards/) – veröffentlichte Tabellen für die Visualisierung nutzen
