---
title: Dokumentschritte
description: Verwalten Sie Dokumente in PlaidCloud-Workflows mit Schritten für Dateikonvertierung, Kopieren, Umbenennen, Löschen und PDF-Operationen.
sidebar:
  label: Dokumentschritte
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

Workflow-Schritte für die Bearbeitung von Dateien, die in Dokumentenkonten gespeichert sind. Verwenden Sie sie, um Dokumente neben Ihren Daten-Workflows zu verschieben, umzuwandeln und zu konvertieren.

## Dateioperationen

- [Copy document file](/de/reference/workflow-steps/document/copy-document-file/) · [Copy document directory](/de/reference/workflow-steps/document/copy-document-directory/)
- [Create document directory](/de/reference/workflow-steps/document/create-document-directory/)
- [Delete document file](/de/reference/workflow-steps/document/delete-document-file/) · [Delete document directory](/de/reference/workflow-steps/document/delete-document-directory/)
- [Verzeichnisliste](/de/reference/workflow-steps/document/directory-listing/) – schreibt eine Tabelle mit den Dateien eines Ordners
- [Update Excel cells](/de/reference/workflow-steps/document/document-excel-update/) – schreibt Werte in ausgewählte Zellen einer Arbeitsmappe oder formatiert sie
- [Fix file extension](/de/reference/workflow-steps/document/fix-file-extension/)
- [Rename document file](/de/reference/workflow-steps/document/rename-document-file/) · [Rename document directory](/de/reference/workflow-steps/document/rename-document-directory/)

Die Schritte zum Kopieren und Umbenennen behandeln eine fehlende Quelle als Normalfall. Fehlt die Datei oder der Ordner, der kopiert oder umbenannt werden soll, oder ist der Ordner leer, tut der Schritt nichts, endet mit einer Warnung, die den Pfad nennt, und der Workflow läuft weiter. Eine geplante Ausführung über einen Ordner, der an diesem Tag keine Dateien enthält, schlägt nicht mehr fehl.

## Verschlüsselung

- [Encrypt file · Decrypt file](/de/reference/workflow-steps/document/encrypt-decrypt-file/) – AES, Blowfish oder ein Kennwort für eine Excel-Arbeitsmappe

## PDF-Operationen

- [Compress PDF](/de/reference/workflow-steps/document/compress-pdf/)
- [Convert image to PDF](/de/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or image to JPEG](/de/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/de/reference/workflow-steps/document/merge-multiple-pdfs/)

## Bildoperationen

- [Crop image to headshot](/de/reference/workflow-steps/document/crop-image-to-headshot/)

## Textoperationen

- [Concatenate files](/de/reference/workflow-steps/document/concatenate-files/) – führt mehrere Dateien zu einer zusammen
- [Document text substitution](/de/reference/workflow-steps/document/document-text-substitution/) – Suchen und Ersetzen in einem Dokument

## Kodierungskonvertierung

- [Convert document encoding](/de/reference/workflow-steps/document/convert-document-encoding/) – Zielkodierung wählen
- [Convert document encoding to ASCII](/de/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert document encoding to UTF-16](/de/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert document encoding to UTF-8](/de/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## Siehe auch

- [Convert Dashboard to PDF](/de/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files](/de/reference/workflow-steps/document/document-delete-old-files/)
- [Dokumentenkonten](/de/guides/documents/adding-accounts/) – verbinden Sie Dokumentenkonten, bevor Sie diese Schritte verwenden
- [Leitfaden zu Dokumenten](/de/guides/documents/) – aufgabenorientierte Anleitungen für dieselben Operationen
