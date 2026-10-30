---
title: Workflow-Fehler auslösen
description: Löst in einem PlaidCloud-Workflow-Schritt einen benutzerdefinierten Fehler aus, um die Fehlerbehandlung zu starten und die Ausführung anzuhalten, wenn Bedingungen nicht erfüllt sind.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## Beschreibung

Versetzt den Workflow mit einer benutzerdefinierten Meldung in einen Fehlerzustand. Verwenden Sie diesen Schritt, wenn ein Schritt den Workflow aufgrund einer Datenbedingung fehlschlagen lassen soll, die frühere Schritte erkannt haben – zum Beispiel „fehlschlagen, wenn die Zeilenanzahl null ist“, „fehlschlagen, wenn eine Validierungstabelle für Schlüssel nicht zugeordnete Werte enthält“ oder „fehlschlagen, wenn eine Saldenprüfung nicht abstimmt“.

Kombinieren Sie ihn mit [Schrittbedingungen](/de/guides/workflows/step-conditions/), damit der Fehler nur ausgelöst wird, wenn tatsächlich etwas nicht stimmt. Wenn der Schritt ausgeführt wird, hält er den Workflow sofort an und schreibt den Fehler in das Workflow-Protokoll. Das kann wiederum den Workflow zur Fehlerbehebung starten, sofern einer konfiguriert ist.


## Workflow-Fehler auslösen


Dieser Schritt ist vor allem für die Verwendung mit Schrittbedingungen gedacht: Er kann so eingestellt werden, dass er ausgeführt wird, wenn Bedingungen erfüllt sind, und einen Fehler im Workflow auslöst.
