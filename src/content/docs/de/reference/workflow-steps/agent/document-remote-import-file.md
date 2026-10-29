---
title: Document - Remote Import File
description: Importieren Sie Dateien in PlaidCloud-Workflows über einen PlaidLink-Agent aus Remote-Systemen, für sicheres Abrufen von Dateien hinter Firewalls.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## Beschreibung



Holt eine Datei über einen PlaidLink-Agent aus einem Remote-Dateisystem und speichert sie in einem PlaidCloud-Dokumentenkonto. Wird verwendet, wenn Quelldateien auf internen Dateifreigaben, lokalen Servern oder hinter einer Firewall liegen.

Der Agent liest die Datei lokal und überträgt sie per Stream an PlaidCloud, wo nachgelagerte Workflow-Schritte sie verarbeiten können.


## Beispiele


Wählen Sie zuerst im Dropdown „Agent to Use“ einen Eintrag aus. Geben Sie als Nächstes unter „File or Folder Path for Import“ den Datei- oder Ordnerpfad ein. Geben Sie dann unter „Folder Destination“ den Zielordner ein. Wählen Sie optional eine **Komprimierung**, um die Datei beim Eingang zu komprimieren: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO oder Deflate (zlib). Wählen Sie abschließend „Save and Run Step“.

## Fehlende Quelldatei oder fehlender Quellordner

Wenn unter dem Pfad auf der Remote-Freigabe nichts existiert, endet der Schritt mit der Warnung `No file or folder found at <path>; nothing imported.` statt mit einem Fehler. Der Workflow wird mit dem nächsten Schritt fortgesetzt, und die Einstellungen des Schritts für Wiederholung und Bei Fehler (zu einem Schritt gehen oder fortfahren) greifen bei einer fehlenden Quelle nicht. Das funktioniert mit den bereits bereitgestellten PlaidLink-Agents.

Ein leerer Pfad endet genauso, mit der Warnung `No path to import from; nothing imported.`. Dazu zählt ein Pfad, dessen Ordner eine Variable ist, die in dieser Ausführung zu nichts aufgelöst wurde, etwa `{folder}/archive`.

Ein Pfad, der ein Dateisystem-Stammverzeichnis oder ein übergeordneter Ordner des Arbeitsverzeichnisses des PlaidLink-Agent ist (`/`, `C:\`, ein Freigabe-Stamm wie `\\server\share` oder `..`), lässt den Schritt fehlschlagen, bevor etwas hochgeladen wird, mit `Refusing to import from the filesystem root <path>.` oder `Refusing to import from <path>, which contains the agent's working directory.` Stammverzeichnisse und `..` werden von den bereits bereitgestellten PlaidLink-Agents abgelehnt; ein aktualisierter Agent lehnt zusätzlich jeden anderen Ordner ab, der sein Arbeitsverzeichnis enthält, beurteilt anhand seines eigenen Dateisystems.

Andere Fehler lassen den Schritt weiterhin fehlschlagen: Zugriff verweigert, ein fehlgeschlagener Upload nach PlaidCloud oder, bei einem aktualisierten PlaidLink-Agent, ein Server oder eine Freigabe, die nicht erreichbar ist.

Da nichts importiert wird, bleibt ein Dokument aus einer früheren Ausführung unverändert bestehen. Um einen nachgelagerten Schritt nur auszuführen, wenn die Datei dieser Periode eingetroffen ist, haben Sie zwei Möglichkeiten:

- Fügen Sie dem nachgelagerten Schritt eine [Schrittbedingung](/de/guides/workflows/step-conditions/#dokumentpfad-bedingungen) **file exists in Document** hinzu, wobei der Document-Pfad auf einen periodenspezifischen Pfad gesetzt ist, etwa einen, der die Periode im Dateinamen enthält.
- Löschen Sie das importierte Dokument, nachdem der Workflow es verwendet hat, damit eine fehlende Quelle keine alte Datei zurücklassen kann.
