---
title: Notify Via Log
description: Schreiben Sie aus einem PlaidCloud-Workflow-Schritt Protokolleinträge, um Statusmeldungen, Debugging-Informationen und Audit-Trail-Ereignisse festzuhalten.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-log.md
---

## Beschreibung


Schreiben Sie eine Nachricht in das Analyze-Workflow-Protokoll.



### Nachrichtenparameter


Geben Sie die Nachricht ein, die in das Protokoll geschrieben werden soll. Wählen Sie dann eine von drei Schweregradstufen aus:


* Information
* Warnung
* Fehler

Bitte beachten Sie, dass sowohl Projektvariablen als auch Workflow-Variablen in dieser Transformation verwendet werden können.


## Beispiele


In diesem Beispiel fügt die Ausführung dieser Transformation dem Protokoll einen Eintrag vom Typ **Information** hinzu, der *Write a message to the workflow log. I believe you have my stapler, Demo.* lautet.
