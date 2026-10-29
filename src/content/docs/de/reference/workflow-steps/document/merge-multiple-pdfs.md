---
title: Merge Multiple PDFs
description: Führen Sie in einem PlaidCloud-Workflow-Schritt mehrere PDF-Dateien zu einem einzigen kombinierten Dokument zusammen, für die Zusammenstellung und Konsolidierung von Berichten.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

Fügt die PDFs in einem Ordner zu einem einzigen PDF zusammen. Anders als [Concatenate files](/de/reference/workflow-steps/document/concatenate-files/) kennt dieser Schritt das PDF-Format und erzeugt ein gültiges zusammengeführtes Dokument.

## Eingaben

- **Eingabeverzeichnis** – der Ordner in einem Dokumentenkonto, dessen PDFs zusammengeführt werden. Stattdessen kann ein einzelnes Archiv angegeben werden, etwa eine ZIP-Datei mit PDFs; die darin enthaltenen PDFs werden zusammengeführt.
- **Zusammengeführte Ausgabedatei** – wohin das zusammengeführte PDF geschrieben wird.

## Funktionsweise

- Die PDFs werden in der Reihenfolge ihres Pfads zusammengeführt, wobei Zahlen nach ihrem Wert behandelt werden – `page2.pdf` steht vor `page10.pdf` –, nummerieren Sie sie also, um die Reihenfolge zu steuern. Jedes behält seine eigenen Seiten in ihrer Reihenfolge.
- Nur Dateien mit der Endung `.pdf` werden zusammengeführt. Alles andere im Ordner bleibt außen vor, und ein Archiv im Ordner wird nicht geöffnet.
- Dateien in Unterordnern werden einbezogen, soweit das Dokumentenkonto sie auflistet: Konten für S3, Wasabi und Google Cloud Storage listen den gesamten Ordnerbaum auf, während OneDrive-, SFTP- und Azure-Konten nur die oberste Ebene auflisten.
- Es werden höchstens 100 PDFs zusammengeführt; bei mehr schlägt der Schritt fehl.

## Ausgabe

Ein einzelnes PDF unter dem Ausgabepfad, das jede Seite jedes zusammengeführten PDFs enthält.

## Hinweise

- Ein Ordner ohne PDFs oder ein nicht vorhandener Ordner beendet den Schritt mit einer Warnung, die den Ordner nennt, führt nichts zusammen, und der Workflow läuft weiter.
- Der Ausgabepfad darf nicht der Eingabepfad sein.

## Typische Einsatzzwecke

- Monatsberichte aus einzelnen Bericht-PDFs zusammenstellen
- Deckblatt, Hauptteil und Anhänge zu einem einzigen Liefergegenstand kombinieren
- Erzeugte Rechnungen zu einem Archiv pro Kunde oder pro Periode bündeln

## Verwandte Themen

- [Compress PDF](/de/reference/workflow-steps/document/compress-pdf/) – verkleinert das zusammengeführte Ergebnis
- [Convert image to PDF](/de/reference/workflow-steps/document/convert-image-to-pdf/) – wandelt Bilder in PDFs um, bevor sie zusammengeführt werden
