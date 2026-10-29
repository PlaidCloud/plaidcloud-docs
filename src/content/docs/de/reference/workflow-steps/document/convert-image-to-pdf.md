---
title: Convert Image to PDF
description: Konvertiert Bilddateien in einem PlaidCloud-Workflow-Schritt in PDF-Dokumente für eine standardisierte Dokumentausgabe und archivfähige Formate.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

Wandelt ein Bild (PNG, GIF, TIFF, JPEG oder HEIC) in eine einseitige PDF um oder passt eine vorhandene PDF an eine Standardseitengröße an.

## Eingaben

- **Eingabedatei oder -verzeichnis** – ein Bild oder eine PDF bzw. ein Ordner damit in einem Dokumentenkonto.
- **Ziel** – hierhin wird die PDF geschrieben.
- **Seitengröße** – US Letter, US Legal, A3, A4 oder A5.
- **Komprimierung** – **Lossy** reduziert Bilder auf Bildschirmauflösung und kann die Datei drastisch verkleinern; **Lossless**, der Standard, behält die Bilddaten exakt bei.

## Funktionsweise

- Ein Bild wird auf einer Seite der gewählten Größe platziert und so skaliert, dass es hineinpasst, ohne seine Proportionen zu ändern. Ein Bild mit mehreren Seiten oder Frames, etwa ein gescanntes TIFF, wird ab dem ersten konvertiert.
- Bei **Lossy** wird das Ergebnis anschließend komprimiert, und eine PDF-Eingabe wird dabei an die gewählte Seitengröße angepasst.
- Bei **Lossless** wird eine PDF-Eingabe unverändert durchgereicht und behält ihre eigene Seitengröße.

## Ausgabe

Eine PDF pro Eingabedatei. Bei einem Ordner wird die PDF jeder Datei unter dem eigenen Namen der Quelldatei in einen Ordner geschrieben, der nach dem Ziel ohne Erweiterung benannt ist. Um mehrere zu einem Dokument zusammenzufassen, lassen Sie auf diesen Schritt [Merge multiple PDFs](/de/reference/workflow-steps/document/merge-multiple-pdfs/) folgen.

## Hinweise

- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, wird der Schritt mit einer Warnung beendet, die den Pfad nennt, und verarbeitet nichts; der Workflow wird fortgesetzt.
- Das Ziel darf nicht der Eingabepfad sein.

## Typische Anwendungen

- Beleg- oder Rechnungsbilder in ein Archivformat vereinheitlichen
- Bildnachweise für Systeme vorbereiten, die nur PDF-Eingaben akzeptieren

## Verwandte Themen

- [Convert PDF or image to JPEG](/de/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF](/de/reference/workflow-steps/document/compress-pdf/)
- [Merge multiple PDFs](/de/reference/workflow-steps/document/merge-multiple-pdfs/)
