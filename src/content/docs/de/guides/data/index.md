---
title: Datenverwaltung – tabellarische Daten
description: Verwalten Sie tabellarische Daten in PlaidCloud mit Tabellen, Ansichten und der leistungsstarken Lakehouse-Engine für die Datenverarbeitung in jeder Größenordnung.
sidebar:
  label: Übersicht
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

Die Datenschicht von PlaidCloud basiert auf **Tabellen** (strukturierte Daten in Zeilen und Spalten) und **Ansichten** (gespeicherte Abfragen über Tabellen). Beide befinden sich innerhalb eines Projekts und werden von der Lakehouse-Engine betrieben, die ohne Konfigurationsänderungen von kleinen Referenztabellen bis zu analytischen Datensätzen mit Milliarden von Zeilen skaliert.

## Inhalt dieses Abschnitts

- [Tabellen und Ansichten](/de/guides/data/tables-views/) – was sie jeweils sind, wann Sie welche verwenden und wie sie zusammenwirken
- [Tabellen-Explorer](/de/guides/data/table-explorer/) – Tabellen in Ihrem Projekt durchsuchen und untersuchen
- [Datentyp Currency](/de/guides/data/currency-data-type/) – ein exakter Spaltentyp mit halber Breite für Geldbeträge und wann Sie ihn statt Numeric wählen sollten
- [Datentyp Vector](/de/guides/data/vector-data-type/) – vorberechnete Embeddings in einer Projekttabelle speichern, die erwartete Breite deklarieren und nach den nächstgelegenen Zeilen suchen
- [Tabellen-Snapshots](/de/guides/data/table-snapshots/) – den Snapshot-Verlauf durchsuchen, Daten zum Stand eines früheren Snapshots anzeigen und eine Tabelle zurücksetzen oder wiederherstellen
- [Das Lakehouse-Fenster](/de/guides/data/lakehouse-window/) – Abfragen beobachten und profilieren, Kataloge und Tabellen mit ihren Snapshots durchsuchen und eine Time-Travel-Abfrage kopieren
- [Daten veröffentlichen](/de/guides/data/publish/) – Projekttabellen für Dashboards, BI-Tools und nachgelagerte Systeme bereitstellen und die zugehörigen Hinweise zur Performance prüfen
- [Den neuesten Datensatz in einer großen Verlaufstabelle auswählen](/de/guides/data/selecting-latest-record-in-large-history-table/) – ein gängiges Muster mit einer performanceorientierten Lösung
- [Geocoding-API](/de/guides/data/geocoding-api/) – eine Geocoding-Integration von Google oder Mapbox auf die REST-Geocoding-Endpunkte von PlaidCloud migrieren
- [Drive-Time-Routing-API](/de/guides/data/drive-time-routing-api/) – Vorschau auf Anfrage: Fahrzeit-Isochronen und Rangfolge nach kürzester Fahrzeit über REST

## Woher die Daten stammen

Tabellen werden in der Regel von **Workflows** befüllt – automatisierten Pipelines, die Daten importieren, transformieren und die Ergebnisse zurückschreiben. Unter [Workflows](/de/guides/workflows/) erfahren Sie, wie Sie sie erstellen, und unter [Referenz der Workflow-Schritte](/de/reference/workflow-steps/) finden Sie jeden verfügbaren Schritttyp.

Informationen zum Anbinden externer Systeme als Datenquellen finden Sie unter [Verbindungen (Leitfaden)](/de/guides/connections/) und [Connectors (Referenz)](/de/reference/connectors/).

## Verwandte Themen

- [Konzepte](/de/get-started/concepts/) – wie Tabellen mit Workflows, Dimensionen und dem übergreifenden Datenmodell zusammenhängen
- [Projekte](/de/guides/projects/) – Projekte besitzen die Tabellen; Tabellen existieren nicht außerhalb eines Projekts
- [Dashboards](/de/guides/dashboards/) – nutzen veröffentlichte Tabellen zur Visualisierung
