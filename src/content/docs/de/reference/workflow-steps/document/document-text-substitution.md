---
title: Document Text Substitution
description: Führen Sie in einem PlaidCloud-Workflow-Schritt Suchen-und-Ersetzen-Vorgänge in Dokumenten aus, um Inhalte automatisiert umzuwandeln.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## Beschreibung

Suchen und Ersetzen in einer Textdatei. Ersetzen Sie bestimmte Zeichenfolgen oder Platzhalter durch neue Werte – nützlich für Vorlagen (einen Platzhalter wie `CUSTOMER_NAME` durch einen tatsächlichen Namen ersetzen) oder zum Bereinigen von Text (bestimmte Zeichenfolgen entfernen oder schwärzen).

Funktioniert mit UTF-8-Textdateien (TXT, CSV, JSON, XML, HTML, RML) beliebiger Größe. Eine Datei, die kein UTF-8-Text ist, etwa ein PDF oder ein Office-Dokument, lässt den Schritt fehlschlagen.

## Eingaben

- **Eingabedatei oder -verzeichnis** – die Datei oder der Ordner mit Dateien, die geändert werden.
- **Zieldatei oder -verzeichnis** – wohin das Ergebnis geschrieben wird. Das Ergebnis wird immer in das Dokumentenkonto der Eingabe geschrieben; das Ziel legt den Pfad fest.
- **Komprimierung** – Keine Komprimierung, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO oder Deflate (zlib) für die Ausgabe. Snappy und LZ4 werden in dem Blockformat geschrieben, das Spark und Hadoop lesen, und LZO als `lzop`-Datei.
- **Reihenfolge der Textersetzungsvorgänge** – eine Zeile pro Ersetzung, jeweils mit dem Originaltext und seiner Ersetzung. In der Ersetzung können Variablen verwendet werden.

## Funktionsweise

- Die Ersetzungen laufen von oben nach unten, und jede arbeitet mit dem Ergebnis der darüberliegenden – eine Ersetzung kann also Text ändern, den eine frühere Zeile eingefügt hat.
- Der Abgleich ist exakt und unterscheidet Groß- und Kleinschreibung; jedes Vorkommen wird ersetzt.
- Eine Zeile mit leerem Originaltext wird ignoriert.
- Bei einem Ordner wird jede Datei unter ihrem eigenen Namen in einen Ordner geschrieben, der nach dem Ziel benannt ist, ohne dessen Erweiterung.
- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, endet der Schritt mit einer Warnung, die den Pfad nennt, verarbeitet nichts, und der Workflow läuft weiter.

## Beispiele

| Original | Ersetzung | `Dear CUSTOMER_NAME,` wird zu |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
