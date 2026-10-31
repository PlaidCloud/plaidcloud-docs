---
title: Workflow ausführen
description: Führt einen vorhandenen Workflow über einen PlaidCloud-Workflow-Schritt aus, um Workflow-Ausführungen zu verketten und Verarbeitungs-Pipelines über mehrere Workflows aufzubauen.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-workflow.md
---

## Beschreibung

Startet im Rahmen der Ausführung des aktuellen Workflows einen anderen Workflow. Verwenden Sie dies, um Workflows zu verketten, wenn ein Prozess logisch von einem anderen abhängt – zum Beispiel ein Workflow „Monatsabschluss“, der einen Workflow „Istwerte laden“, dann einen Workflow „Umlagen ausführen“ und schließlich einen Workflow „Dashboards veröffentlichen“ aufruft.

Der aufgerufene Workflow läuft unabhängig – er kann im selben oder in einem anderen Projekt liegen. Standardmäßig fährt der aufrufende Workflow fort, ohne zu warten. Aktivieren Sie die Option **Wait until processing completes**, wenn die nächsten Schritte im Aufrufer davon abhängen, dass der aufgerufene Workflow zuerst abgeschlossen ist.



## Auszuführender Workflow


Wählen Sie zunächst im Dropdown-Menü **Projekt** das Projekt aus, das den auszuführenden Workflow enthält.



Wählen Sie anschließend im Dropdown-Menü **Workflow** den Workflow aus, der ausgeführt werden soll.



Zusätzlich gibt es die Option **Wait until processing completes before continuing.** Wenn Sie dieses Kontrollkästchen aktivieren, wird die Ausführung des aktuellen Workflows zurückgestellt, bis der aufgerufene Workflow seine Ausführung abgeschlossen hat. Standardmäßig ist diese Option deaktiviert. Das bedeutet, dass der aktuelle Workflow, in dem sich diese Transformation befindet, parallel zum aufgerufenen Workflow weiterverarbeitet wird.







## Beispiele

Noch keine Beispiele ...
