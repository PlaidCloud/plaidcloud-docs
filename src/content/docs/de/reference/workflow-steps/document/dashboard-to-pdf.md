---
title: Convert Dashboard to PDF
description: Rendern Sie ein PlaidCloud-Dashboard als PDFs in ein Dokumentenkonto – einmal pro Zeile eines Filter-Datasets, wobei die Werte jeder Zeile als Filter des Dashboards angewendet werden.
sidebar:
  order: 22
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/dashboard-to-pdf.md
---

## Beschreibung

Rendert ein Dashboard als PDFs und schreibt sie in ein Dokumentenkonto. Damit stellen Sie ein Dashboard auf einen Zeitplan – für ein Monatsabschluss-Paket, die Verteilung an Personen, die sich nicht anmelden, oder einen archivierten Snapshot dessen, wie die Zahlen an einem bestimmten Tag aussahen.

Der Schritt rendert einmal pro Zeile eines Filter-Datasets und wendet die Werte dieser Zeile als Filter des Dashboards an. So erzeugt ein einzelner Schritt in einer Ausführung einen Satz PDFs pro Region oder pro Entität.

## Konfiguration

### Dashboard

Das Dashboard, das gerendert wird.

### Filter-Dataset

Die Tabelle, deren Zeilen die Renderings steuern: ein PDF pro Zeile.

### Ausgabepfad

Das Dokumentenkonto und der Ordner, in die die PDFs geschrieben werden.

### Optionen

- **Parallele PDF-Erstellung** – wie viele Renderings gleichzeitig laufen. Der Standard ist 8; verringern Sie den Wert, wenn das Dashboard so aufwendig ist, dass parallele Renderings in Zeitüberschreitungen laufen.
- **Renderwartezeit (Sekunden)** – in der Schrittkonfiguration vorhanden, wird vom Workflow-Runner aber **derzeit nicht angewendet**. Die Einstellung hat heute keine Wirkung.

### Dashboard-Filter

Die eigenen Filter des Dashboards, jeweils mit ihrer **Dashboard-Filter-ID**. Sie werden aus dem Dashboard gelesen, wenn Sie die Zuordnung füllen.

### Quellspaltenzuordnung

Die Spalten des Filter-Datasets und wie jede davon verwendet wird. Mit **Quelle untersuchen › Zuordnungstabelle füllen** lesen Sie die Spalten und die Filter des Dashboards ein; eine Spalte, die wie ein Dashboard-Filter heißt, wird als Filter dafür markiert. Beim erneuten Füllen bleiben die Werte für **Art** und **Zugeordnete Filterspalte** erhalten, die Sie für eine Spalte bereits festgelegt haben.

Legen Sie für jede Spalte die **Art** fest:

- **Spaltenfilter** – der Wert der Spalte setzt den Dashboard-Filter, der unter **Zugeordnete Filterspalte** genannt ist; dieser muss einer der Filter des Dashboards sein.
- **Dateiname** – die Spalte liefert den Dateinamen jedes PDFs. Nur eine Spalte kann der Dateiname sein. Ohne eine solche Spalte gibt der Schritt eine Warnung aus und erzeugt die Namen automatisch.
- **Kein Filter** – die Spalte wird nicht verwendet.

Mindestens eine Spalte muss ein **Spaltenfilter** sein.

## Was beim Speichern geprüft wird

Das Speichern des Schritts wird unter Nennung der Spalte abgelehnt, wenn:

- keine Spalte ein Spaltenfilter mit einer Zugeordneten Filterspalte ist – *Kennzeichnen Sie mindestens eine Quellspalte als Spaltenfilter, mit der Zugeordneten Filterspalte, die sie setzt.*
- ein Spaltenfilter keine Zugeordnete Filterspalte hat oder eine nennt, die nicht zu den Filtern des Dashboards gehört – *Die Zugeordnete Filterspalte 'Region' für die Quellspalte 'region' ist keiner der Filter des Dashboards.*
- mehr als eine Spalte der Dateiname ist – *Nur eine Quellspalte kann der Dateiname sein; region, entity sind es alle.*
- eine Spalte vom Typ Spaltenfilter oder Dateiname keinen Datentyp hat – *Die Quellspalte 'region' hat keinen Datentyp; untersuchen Sie die Quelle erneut, um ihn zu aktualisieren.* Bei manchen im Schrittformular gespeicherten Schritten fehlen die Typen ihrer Spalten, und sie schlagen bei jeder Ausführung fehl, bis die Typen wieder vorhanden sind. Führen Sie **Quelle untersuchen › Zuordnungstabelle füllen** aus, um sie wiederherzustellen; Ihre Markierungen als Spaltenfilter und Dateiname bleiben erhalten.

## Verwandte Themen

- [Dokumentschritte](/de/reference/workflow-steps/document/)
- [Dashboards (Leitfaden)](/de/guides/dashboards/)
- [Berichtsschritte](/de/reference/workflow-steps/reports/)
