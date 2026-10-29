---
title: Compress PDF
description: Komprimiert PDF-Dateien in einem PlaidCloud-Workflow-Schritt, um die Dateigröße zu verringern und dabei die Dokumentqualität für eine effiziente Speicherung zu erhalten.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

Verringert die Dateigröße einer PDF, die in einem Dokumentenkonto gespeichert ist. Nützlich, um große gescannte Dokumente vor der Archivierung, vor dem Anhängen an Benachrichtigungen oder vor dem Verschieben zwischen Dokumentenkonten zu verkleinern.

## Eingaben

- **Eingabedatei oder -verzeichnis** – eine PDF oder ein Ordner mit PDFs in einem Dokumentenkonto.
- **Ausgabedatei oder -verzeichnis** – hierhin wird die komprimierte PDF geschrieben.

## Funktionsweise

Die PDF wird neu geschrieben, wobei ihre Bilder auf Bildschirmauflösung (72 dpi) reduziert und ihre Schriftarten als Teilmengen eingebettet werden. Das kann gescannte Dokumente drastisch verkleinern; Text bleibt scharf. Die Seiten werden auf das Format US Letter angepasst.

## Ausgabe

Eine komprimierte PDF am Ausgabepfad. Bei einem Ordner wird jede PDF unterhalb des Ausgabepfads geschrieben und behält dabei ihre Position relativ zum Eingabeordner.

## Hinweise

- Der Ausgabepfad darf nicht der Eingabepfad sein, sodass die Quelle nie überschrieben wird.
- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, wird der Schritt mit einer Warnung beendet, die den Pfad nennt, und verarbeitet nichts; der Workflow wird fortgesetzt.
- Eine PDF, die sich nicht komprimieren lässt, lässt den Schritt fehlschlagen, unter Nennung der Datei und des Grundes.

## Typische Anwendungen

- Gescannte Rechnungen, Belege oder Verträge vor der Langzeitspeicherung verkleinern
- PDF-Größe vor dem Versand per E-Mail oder dem Anhängen an Benachrichtigungen verringern
- Dokumente für den Upload in nachgelagerte Systeme mit Größenbeschränkung vorbereiten

## Verwandte Themen

- [Convert PDF or image to JPEG](/de/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/de/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Leitfaden zu Dokumenten](/de/guides/documents/)
