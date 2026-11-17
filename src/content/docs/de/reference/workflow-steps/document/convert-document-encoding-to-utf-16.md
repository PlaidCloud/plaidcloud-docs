---
title: Convert Document Encoding to UTF-16
description: Konvertiert die Kodierung einer Dokumentdatei in einem PlaidCloud-Workflow-Schritt nach UTF-16, um Mehrbyte-Zeichensätze und Unicode-Text zu unterstützen.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## Beschreibung

Schreibt eine Textdatei in UTF-16 neu. Nützlich, wenn ein nachgelagertes System UTF-16 verlangt oder wenn eine Quelle Kodierungen mischt, die andere Tools ablehnen.

## Eingaben

- **Eingabedatei oder -verzeichnis** – die Textdatei oder komprimierte Datei oder ein Ordner mit solchen Dateien, die konvertiert werden sollen.
- **Ziel** – hierhin wird die konvertierte Datei geschrieben.
- **Komprimierung** – Keine Komprimierung, Zip, GZip oder BZip2 für die Ausgabe.
- **Unterordner beibehalten** – bei einem Ordner aktivieren, um jede Datei aus einem Unterordner in den entsprechenden Unterordner des Ziels zu schreiben.
- **Endianness (Byte-Reihenfolge)** – Little Endian oder Big Endian.
- **Include BOM** – aktivieren, damit die Datei mit einer Byte-Order-Mark beginnt (`FF FE` für Little Endian, `FE FF` für Big Endian). Deaktiviert lassen für keine Markierung.

## Funktionsweise

- Die Kodierung der Quelle wird erkannt. Eine UTF-8-Datei wird als UTF-8 gelesen, und Windows-Zeichen, die in eine solche Datei eingefügt wurden – etwa typografische Anführungszeichen aus Word oder Excel –, bleiben unabhängig von ihrer Anzahl intakt. Eine Datei in einer anderen Kodierung wird in der Kodierung gelesen, die anhand ihres ersten Abschnitts erkannt wird, der kein gültiges UTF-8 ist.
- Der Text wird unverändert geschrieben – Buchstaben mit Akzent, Symbole und andere Zeichen bleiben genau so erhalten, wie sie waren.
- Eine Datei, deren Kodierung nicht erkannt werden kann, lässt den Schritt fehlschlagen, unter Nennung der Datei.
- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, wird der Schritt mit einer Warnung beendet, die den Pfad nennt, und verarbeitet nichts; der Workflow wird fortgesetzt.
- Eine komprimierte Datei – etwa eine Zip-, GZip- oder BZip2-Datei – wird zuerst entpackt, und jede darin enthaltene Datei wird konvertiert.
- Bei einem Ordner wird jede Datei konvertiert und unter ihrem eigenen Namen in das Ziel geschrieben. Aktivieren Sie **Unterordner beibehalten**, um stattdessen eine Datei aus einem Unterordner in den entsprechenden Unterordner des Ziels zu schreiben; der Inhalt einer komprimierten Datei geht dann in den Unterordner, in dem die komprimierte Datei lag.
- Würden zwei Dateien an dieselbe Stelle im Ziel geschrieben, schlägt der Schritt fehl, bevor er die zweite schreibt, statt sie die erste ersetzen zu lassen. Die Meldung nennt beide Dateien oder die komprimierte Datei, aus der beide stammen, sowie die Stelle; würde das Aktivieren von **Unterordner beibehalten** sie an getrennten Stellen ablegen, weist sie darauf hin.

## Beispiele

Wählen Sie die Eingabedatei aus und navigieren Sie an ihrem Speicherort zur Datei. Wählen Sie den gewünschten Ausgabeort, legen Sie die Byte-Reihenfolge fest und aktivieren Sie **Include BOM**, wenn das empfangende System eine Markierung erwartet. Speichern und ausführen.
