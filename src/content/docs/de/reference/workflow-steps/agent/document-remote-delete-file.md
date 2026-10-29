---
title: Document - Remote Delete File
description: Löschen Sie Dateien auf Remote-Systemen in PlaidCloud-Workflows über einen PlaidLink-Agent, für sichere Dateiverwaltung hinter Firewalls.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## Beschreibung



Löscht eine Datei auf einem Dateisystem hinter einer Firewall, das über einen PlaidLink-Agent erreicht wird. Der Agent führt das Löschen lokal auf dem lokalen Dateisystem aus.

Verwenden Sie ihn für die Bereinigung nach lokalen Exportvorgängen oder als Teil dateibasierter Integrationen, die verarbeitete Quelldateien entfernen müssen.


## Beispiele


Wählen Sie zuerst im Dropdown „Agent to Use“ einen Eintrag aus. Geben Sie als Nächstes unter „File or Folder Path for Delete“ den Datei- oder Ordnerpfad ein. Wählen Sie abschließend „Save and Run Step“.

## Fehlender Pfad

Mit einem aktualisierten PlaidLink-Agent beendet ein Pfad, der auf dem Remote-System nicht existiert, den Schritt mit der Warnung `Nothing to delete at <path>` statt mit einem Fehler, und der Workflow wird fortgesetzt. Agents, die nicht aktualisiert wurden, lassen den Schritt weiterhin fehlschlagen.

Ein leerer Pfad beendet den Schritt mit der Warnung `No path to delete; nothing deleted.` und löscht nichts. Dazu zählt ein Pfad, dessen Ordner eine Variable ist, die in dieser Ausführung zu nichts aufgelöst wurde, etwa `{folder}/archive`.

Ein Pfad, der ein Dateisystem-Stammverzeichnis oder ein übergeordneter Ordner des Arbeitsverzeichnisses des PlaidLink-Agent ist (`/`, `C:\`, ein Freigabe-Stamm wie `\\server\share` oder `..`), lässt den Schritt fehlschlagen, bevor etwas gelöscht wird, mit `Refusing to delete the filesystem root <path>.` oder `Refusing to delete <path>, which contains the agent's working directory.` Stammverzeichnisse und `..` werden von den bereits bereitgestellten PlaidLink-Agents abgelehnt; ein aktualisierter Agent lehnt zusätzlich jeden anderen Ordner ab, der sein Arbeitsverzeichnis enthält, beurteilt anhand seines eigenen Dateisystems.
