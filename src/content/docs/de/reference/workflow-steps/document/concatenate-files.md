---
title: Concatenate Files
description: Verkettet in einem PlaidCloud-Workflow-Schritt mehrere Dateien zu einer einzigen Datei, um Text-, CSV- oder andere Dokumentausgaben zusammenzuführen.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

Fasst zwei oder mehr Dateien in einem Dokumentenkonto zu einer einzigen Ausgabedatei zusammen. Arbeitet Byte für Byte – nützlich für reine Textformate (CSV, Protokolldateien, JSON Lines), bei denen einfaches Verketten eine gültige Ausgabe erzeugt.

## Eingaben

- **Quelldateien** – Liste der zu verkettenden Dateien, in der Reihenfolge
- **Ausgabepfad** – Ziel der zusammengeführten Datei
- **Trennzeichen** – optionale Bytefolge, die zwischen die Quelldateien eingefügt wird (häufig ein Zeilenumbruch)

## Ausgabe

Eine einzelne Datei mit dem Inhalt aller Quelldateien in der angegebenen Reihenfolge, verbunden durch das konfigurierte Trennzeichen.

Eine Quelldatei, die nicht existiert, wird in der zusammengeführten Datei ausgelassen, und der Schritt wird mit einer Warnung beendet, die sie nennt; der Workflow wird fortgesetzt.

## Typische Anwendungen

- Tägliche Protokolldateien zu einem Monatsarchiv zusammenführen
- CSV-Dateien mit gleichem Schema zusammenführen (Kopfzeilen bis auf die erste entfernen)
- JSON-Lines-Exporte aus mehreren Quellen vor der Verarbeitung verbinden

## Nicht geeignet für

- PDFs – verwenden Sie stattdessen [Merge multiple PDFs](/de/reference/workflow-steps/document/merge-multiple-pdfs/)
- Binärformate mit Headern (XLSX, ZIP, Bilddateien) – das Verketten von Bytes erzeugt keine gültige Datei

## Verwandte Themen

- [Merge multiple PDFs](/de/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Leitfaden zu Dokumenten](/de/guides/documents/)
