---
title: Document - Remote Rename File
description: Benennen Sie Dateien auf Remote-Systemen in PlaidCloud-Workflows über einen PlaidLink-Agent um, für sichere Dateiverwaltung hinter Firewalls.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## Beschreibung



Benennt eine Datei auf einem Remote-Dateisystem über einen PlaidLink-Agent um oder verschiebt sie. Arbeitet ausschließlich auf der lokalen Seite; es werden keine Daten von oder nach PlaidCloud übertragen.

Übliches Muster: Eine Quelldatei nach einem erfolgreichen Remote-Import-Schritt umbenennen, um sie als „verarbeitet“ zu kennzeichnen, damit derselbe Workflow sie bei der nächsten Ausführung nicht erneut importiert.


## Beispiele


Wählen Sie zuerst im Dropdown „Agent to Use“ einen Eintrag aus. 



Geben Sie als Nächstes „Source Path“ und „Destination Path“ ein. 



Wählen Sie abschließend „Save and Run Step“.

## Fehlende Quelle

Mit einem aktualisierten PlaidLink-Agent beendet eine Quelle, die auf dem Remote-System nicht existiert, den Schritt mit der Warnung `No file or folder found at <path>; nothing renamed` statt mit einem Fehler, und der Workflow wird fortgesetzt. Agents, die nicht aktualisiert wurden, lassen den Schritt weiterhin fehlschlagen.

Ein leerer Quellpfad beendet den Schritt mit der Warnung `No path to rename from; nothing renamed.`, auch wenn ein Ordner im Pfad eine Variable ist, die in dieser Ausführung zu nichts aufgelöst wurde.

Eine Quelle, die ein Dateisystem-Stammverzeichnis oder ein übergeordneter Ordner des Arbeitsverzeichnisses des PlaidLink-Agent ist (`/`, `C:\`, ein Freigabe-Stamm wie `\\server\share` oder `..`), lässt den Schritt mit `Refusing to rename from the filesystem root <path>.` oder `Refusing to rename from <path>, which contains the agent's working directory.` fehlschlagen. Ein leerer Zielpfad lässt den Schritt mit `No destination path for the rename; it would write into the agent's working directory.` fehlschlagen. Das Umbenennen in ein Laufwerks- oder Freigabe-Stammverzeichnis wie `E:\` oder `\\nas\drop` funktioniert. Stammverzeichnisse und `..` werden von den bereits bereitgestellten PlaidLink-Agents abgelehnt; ein aktualisierter Agent lehnt zusätzlich jeden anderen Ordner ab, der sein Arbeitsverzeichnis enthält, beurteilt anhand seines eigenen Dateisystems.
