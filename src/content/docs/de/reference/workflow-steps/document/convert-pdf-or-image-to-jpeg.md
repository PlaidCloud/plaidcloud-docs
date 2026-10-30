---
title: Convert PDF or Image to JPEG
description: Konvertiert PDF-Seiten oder Bilder in einem PlaidCloud-Workflow-Schritt in das JPEG-Format für webkompatible Ausgaben und Bildverarbeitungsaufgaben.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

Konvertiert eine PDF oder ein Bild in ein JPEG. Die erste Seite einer PDF wird zum JPEG; ein Bild wird neu kodiert, und ein Bild mit mehreren Seiten oder Frames, etwa ein gescanntes TIFF, wird ab dem ersten konvertiert.

## Eingaben

- **Eingabedatei oder -verzeichnis** – eine PDF oder ein Bild (PNG, GIF, TIFF, JPEG oder HEIC) bzw. ein Ordner damit in einem Dokumentenkonto.
- **Ausgabedatei oder -verzeichnis** – hierhin wird das JPEG geschrieben.

## Ausgabe

Ein JPEG pro Eingabedatei. Bei einem Ordner wird das JPEG jeder Datei unter dem eigenen Namen der Quelldatei in einen Ordner geschrieben, der nach dem Ausgabepfad ohne Erweiterung benannt ist.

## Hinweise

- Eine Datei eines anderen Typs lässt den Schritt fehlschlagen, unter Nennung der akzeptierten Typen.
- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, wird der Schritt mit einer Warnung beendet, die den Pfad nennt, und verarbeitet nichts; der Workflow wird fortgesetzt.
- Der Ausgabepfad darf nicht der Eingabepfad sein.

## Typische Anwendungen

- Vorschaubilder für die Webanzeige erzeugen
- Reine Bildversionen von PDFs für Systeme erstellen, die kein PDF verarbeiten können

## Verwandte Themen

- [Convert image to PDF](/de/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF](/de/reference/workflow-steps/document/compress-pdf/)
- [Crop image to headshot](/de/reference/workflow-steps/document/crop-image-to-headshot/)
