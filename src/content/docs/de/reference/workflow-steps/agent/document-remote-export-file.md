---
title: Document - Remote Export File
description: Exportieren Sie Dateien in PlaidCloud-Workflows über einen PlaidLink-Agent auf Remote-Systeme, für sichere Dateiübertragungen hinter Firewalls.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## Beschreibung



Schreibt eine Datei aus einem PlaidCloud-Dokumentenkonto über einen PlaidLink-Agent auf ein Remote-Dateisystem. Nützlich, um Berichte, Extrakte oder verarbeitete Dateien an Systeme zu liefern, die von PlaidCloud aus nicht direkt erreichbar sind — interne Netzlaufwerke, lokale SFTP-Server oder spezialisierte Anwendungsverzeichnisse.

Der Agent empfängt die Datei von PlaidCloud und schreibt sie an das konfigurierte lokale Ziel.


## Beispiele


Wählen Sie zuerst im Dropdown „Agent to Use“ einen Eintrag aus. Suchen Sie als Nächstes unter „File or Folder to Export“ den Datei- oder Ordnerpfad. Geben Sie dann unter „Export Path Destination“ den Speicherort ein. Wählen Sie abschließend „Save and Run Step“.

## Pfadsicherheit

Ein leerer Exportpfad lässt den Schritt mit `No destination path for the export; it would write into the agent's working directory.` fehlschlagen. Dazu zählt ein Pfad, der zu nichts aufgelöst wurde, weil eine Variable darin leer war. Der Export in ein Laufwerks- oder Freigabe-Stammverzeichnis wie `E:\` oder `\\nas\drop` funktioniert.

Ist **Archiv bei Eingang entpacken** ausgewählt, entpackt der Schritt jedes Archiv im Zielordner und entfernt es. Er lehnt daher ein Ziel ab, das ein Dateisystem-Stammverzeichnis oder eine Datei direkt darin ist (`Refusing to unpack an export into the filesystem root <path>.`), oder den eigenen Ordner des PlaidLink-Agent (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Wählen Sie stattdessen einen eigenen Unterordner.

Die Prüfungen auf leere Pfade und Stammverzeichnisse funktionieren mit den bereits bereitgestellten PlaidLink-Agents. Die Ablehnung des eigenen Ordners des Agents erfordert einen aktualisierten PlaidLink-Agent.
