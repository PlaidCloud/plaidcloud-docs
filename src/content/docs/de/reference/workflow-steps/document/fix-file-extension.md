---
title: Fix File Extension
description: Korrigieren Sie in einem PlaidCloud-Workflow-Schritt Dateierweiterungen, indem der tatsächliche Dateityp erkannt und die Datei mit der passenden Erweiterung umbenannt wird.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

Liest, was eine Datei tatsächlich enthält, und benennt sie, wo dies ihrer Erweiterung widerspricht, mit der Erweiterung um, die ihr Typ üblicherweise trägt – ein als `.dat` gespeichertes PDF wird zu `.pdf`. Nützlich, wenn ein Quellsystem Dateien mit falschen oder fehlenden Erweiterungen übergibt.

## Eingaben

- **Eingabedatei oder -verzeichnis** – eine Datei oder ein Ordner, dessen Dateien jeweils geprüft werden, in einem Dokumentenkonto. Dateien werden an Ort und Stelle umbenannt, daher gibt es keinen Ausgabeort.

## Funktionsweise

Der Schritt erkennt den Typ jeder Datei anhand ihres Inhalts und benennt die Datei nur um, wenn ihrem aktuellen Namen eine Erweiterung fehlt, er eine Platzhalter-Erweiterung (`.dat`, `.tmp` oder `.bin`) hat oder einen anderen Typ nennt, den der Schritt erkennt.

Die erkannten Typen sind PDF; Bilder in JPEG, PNG, GIF, TIFF, BMP, WebP und HEIC; Excel- (`.xlsx`, `.xls`), Word- (`.docx`, `.doc`) und PowerPoint-Dokumente (`.pptx`); ZIP- und GZip-Archive sowie CSV, JSON, HTML, XML und Nur-Text.

Eine Datei behält ihren Namen, wenn:

- ihre Erweiterung bereits zum Inhalt passt – `.jpg` und `.jpeg` passen beide zu einem JPEG, `.tif` und `.tiff` zu einem TIFF;
- ihre Erweiterung eine ist, die der Schritt nicht erkennt, etwa `.sql`, `.log` oder `.ai`, weil der Inhalt allein ein SQL-Skript nicht von anderem Text oder eine Illustrator-Datei nicht von einem PDF unterscheiden kann;
- sie Nur-Text unter einer Textendung wie `.csv`, `.tsv` oder `.json` enthält;
- sie ein Textformat unter der Erweiterung eines anderen enthält – XML in einer `.html`-Datei, CSV in einer `.json`-Datei – weil sich diese anhand des Inhalts nicht zuverlässig unterscheiden lassen. Nur eine `.txt`-Datei oder eine ohne oder mit Platzhalter-Erweiterung wird in ein Textformat umbenannt;
- sie eine ZIP-Datei ist, die wie ein Office-Dokument benannt ist, da `.xlsx`-, `.docx`- und `.pptx`-Dateien intern ZIP-Dateien sind;
- ihr Typ sich nicht bestimmen lässt, etwa bei einer leeren Datei.

Ein Archiv wird nach seinem eigenen Inhalt beurteilt: Seine Mitglieder werden weder geöffnet noch umbenannt. Dateien, deren Name mit `.` beginnt, werden übersprungen.

## Beispiele

| Datei | Inhalt | Ergebnis |
|---|---|---|
| `invoice.dat` | PDF | umbenannt in `invoice.pdf` |
| `photo.png` | JPEG | umbenannt in `photo.jpg` |
| `export.txt` | CSV | umbenannt in `export.csv` |
| `readme` | Nur-Text | umbenannt in `readme.txt` |
| `query.sql` | Nur-Text | unverändert |
| `budget.xlsx` | ZIP | unverändert |

## Hinweise

- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, endet der Schritt mit einer Warnung, die den Pfad nennt, verarbeitet nichts, und der Workflow läuft weiter.

## Verwandte Themen

- [Concatenate files](/de/reference/workflow-steps/document/concatenate-files/)
- [Leitfaden zu Dokumenten](/de/guides/documents/)
