---
title: LLM-Schritt
description: Führen Sie einen Prompt gegen ein LLM mit eingeschränktem Lese- und/oder Schreibzugriff auf Projektdaten aus, wobei das Modell seine Ergebnisse direkt über den MCP-Server zurückschreibt.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## Beschreibung

Der **LLM-Schritt** sendet einen Prompt an ein großes Sprachmodell. Mit einer Anthropic-LLM-Verbindung erhält das Modell eingeschränkten Zugriff auf die Projekttabellen, Dimensionen und Dokumente, die Sie binden — **Lesen**, **Schreiben** oder beides pro Objekt — und schreibt seine Ergebnisse direkt in die Bindungen mit Schreibberechtigung. Eine Schreibbindung ist die Ausgabe des Schritts; es gibt kein separates Ausgabeformat.

Eine vollständige Anleitung finden Sie im [Leitfaden zum LLM-Schritt](/de/guides/workflows/llm-step/).

## Konfiguration

* **LLM-Verbindung** *(erforderlich)* — eine Verbindung vom Typ LLM (zum Beispiel Anthropic). Ihr **Agent-Zugriff** muss für jede Schreibbindung **Lesen und Schreiben** sein. **Vollständig** erlaubt Schreibvorgänge ebenfalls, bis es am 15. Januar 2027 entfernt wird, und ein Schritt, der es verwendet, protokolliert beim Abschluss eine Warnung. Bei **Lesen und Schreiben** schreibt ein Schritt nur in Bindungen mit aktiviertem Schreiben und kann weder schreibendes SQL ausführen noch Tabellen erstellen.
* **Modell** *(optional)* — standardmäßig das Standardmodell der Verbindung. Mit einer Anthropic-Verbindung funktioniert jedes Claude-Modell, auch ältere Modelle wie Claude Sonnet 4.5.
* **Prompt** *(erforderlich)* — unterstützt die Verweise `{{tables.NAME}}`, `{{dimensions.NAME}}` und `{{documents.NAME}}` auf gebundene Objekte.
* **Ergebnisschema** *(bei Anthropic optional; bei anderen Anbietern erforderlich)* — ein JSON-Schema (Root `"type": "object"`) für eine erfasste strukturierte Zusammenfassung. Lassen Sie es bei Anthropic leer, wenn die Arbeit des Modells aus seinen MCP-Schreibvorgängen besteht. Anbieter außer Anthropic haben keinen MCP-Zugriff, daher ist ein Schema erforderlich.
* **Bindungen** — Tabellen, Dimensionen und Dokumente, auf die das Modell zugreifen darf, jeweils über eine Auswahl gewählt und mit **Lesen** und/oder **Schreiben** versehen. Schreibtabellen erhalten eingefügte Zeilen, Schreibdimensionen erhalten Knoten, Schreibdokumente erhalten hochgeladene Dateien.
* **Limits** — Maximale Ausgabetokens (1.024 bis 128.000) und Credential TTL (60 bis 3.600 Sekunden).

## Verhalten

* Der Modellaufruf läuft in einem eigenen Job. Für die Ausführung wird ein kurzlebiger, eingeschränkter Berechtigungsnachweis erzeugt, der am Ende widerrufen wird.
* Der Zugriff wird pro Objekt und pro Kontrollkästchen gesteuert: Das Modell liest nur lesegebundene Objekte und schreibt nur schreibgebundene — nie ein Objekt, das Sie nicht gebunden haben. Das Schreiben erfordert ein vorhandenes Zielobjekt; der Schritt erstellt keines.
* Jede Ausführung löst einen kostenpflichtigen Anbieteraufruf aus und schreibt in Ihre gebundenen Objekte.

## Was beim Speichern geprüft wird

* **Ergebnisschema** — wenn Sie eines angeben, muss es gültiges JSON und ein JSON-Objekt sein und an seiner Wurzel `"type": "object"` deklarieren. Andernfalls wird das Speichern abgelehnt, zum Beispiel mit *The result schema must declare "type": "object" at its root.*
* **Bindungen und die Verbindung** — nur eine Anthropic-Verbindung gibt dem Modell Zugriff auf Bindungen. Das Speichern eines Schritts mit Bindungen bei der Verbindung eines anderen Anbieters wird abgelehnt, mit einer Meldung, die den Anbieter nennt und dazu auffordert: *Remove the bindings or choose an Anthropic connection.* Eine Bindung mit aktiviertem **Schreiben** benötigt eine Verbindung, deren **Agent-Zugriff** Schreibvorgänge erlaubt. Bei einer Verbindung mit reinem Lesezugriff wird das Speichern abgelehnt mit *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* Ein über die API ohne Verbindung gespeicherter Schritt wird gegen die Standard-LLM-Verbindung des Workspace geprüft, auf der er auch läuft: die von einem Admin als Standard markierte oder sonst die zuletzt aktualisierte. Ohne einen von einem Admin markierten Standard macht das Bearbeiten einer anderen LLM-Verbindung diese zum Standard und kann das nächste Speichern des Schritts ablehnen.
