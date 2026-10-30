---
title: Crop Image to Headshot
description: Beschneidet Bilder in einem PlaidCloud-Workflow-Schritt zu einem quadratischen Porträtfoto für einheitliche Porträts in Verzeichnissen und auf Ausweisen.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

Beschneidet ein Bild zu einem zentrierten Quadrat und skaliert es auf ein JPEG mit 500 × 500 Pixeln. Nützlich, um Mitarbeiter- oder Mitgliederverzeichnisse zu vereinheitlichen, in denen die Quellfotos unterschiedliche Seitenverhältnisse haben.

## Eingaben

- **Eingabedatei oder -verzeichnis** – ein Bild oder ein Ordner mit Bildern in einem Dokumentenkonto.
- **Ausgabedatei oder -verzeichnis** – hierhin wird das Porträtfoto geschrieben.

## Ausgabe

Ein JPEG mit 500 × 500 Pixeln, aus der Mitte der Quelle beschnitten. Bei einem Ordner wird das Porträtfoto jeder Datei in einen Ordner geschrieben, der nach dem Ausgabepfad ohne Erweiterung benannt ist.

## Hinweise

- Der Ausschnitt wird aus der Bildmitte genommen; es wird kein Gesicht gesucht, daher sollten Sie Quellfotos so wählen, dass die Person zentriert ist.
- Eine Datei, die sich nicht als Bild lesen lässt, wird unverändert in die Ausgabe kopiert, statt den Schritt fehlschlagen zu lassen.
- Wenn der Eingabepfad nicht existiert oder keine Dateien enthält, wird der Schritt mit einer Warnung beendet, die den Pfad nennt, und verarbeitet nichts; der Workflow wird fortgesetzt.
- Der Ausgabepfad darf nicht der Eingabepfad sein.

## Typische Anwendungen

- Fotos in Mitarbeiterverzeichnissen vereinheitlichen
- Einheitliche Avatarbilder für ein internes Portal erzeugen
- Fotos für Ausweise und Berechtigungsnachweise zuschneiden

## Verwandte Themen

- [Convert PDF or image to JPEG](/de/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix file extension](/de/reference/workflow-steps/document/fix-file-extension/)
