---
title: Convert Document Encoding to ASCII
description: Konvertiert die Kodierung einer Dokumentdatei in einem PlaidCloud-Workflow-Schritt nach ASCII, um die Kompatibilität mit Systemen sicherzustellen, die ASCII-Text benötigen.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-ascii.md
---

## Beschreibung

Schreibt eine Textdatei als reinen ASCII-Text neu. Das ist besonders nützlich, wenn die Informationsquelle gemischte Kodierungen enthält oder andere Tools bestimmte Kodierungen nicht unterstützen.

## Funktionsweise

- Die Kodierung der Quelle wird erkannt. Eine UTF-8-Datei wird als UTF-8 gelesen, und Windows-Zeichen, die in eine solche Datei eingefügt wurden – etwa typografische Anführungszeichen aus Word oder Excel –, bleiben unabhängig von ihrer Anzahl intakt. Eine Datei in einer anderen Kodierung wird in der Kodierung gelesen, die anhand ihres ersten Abschnitts erkannt wird, der kein gültiges UTF-8 ist.
- Buchstaben mit Akzent behalten ihren Grundbuchstaben (`café` wird zu `cafe`), und Zeichen ohne ASCII-Form werden verworfen.
- Eine Zeile, die nur ein doppeltes Anführungszeichen enthält, wird an das Ende der vorhergehenden Zeile angehängt.
- Eine Datei, deren Kodierung nicht erkannt werden kann, lässt den Schritt fehlschlagen, unter Nennung der Datei.
- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, wird der Schritt mit einer Warnung beendet, die den Pfad nennt, und verarbeitet nichts; der Workflow wird fortgesetzt.

## Beispiele

Wählen Sie die Eingabedatei aus und navigieren Sie an ihrem Speicherort zur Datei. Wählen Sie den gewünschten Ausgabeort und navigieren Sie zum gewünschten Speicherort der Datei. Speichern und ausführen.
