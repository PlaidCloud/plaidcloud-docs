---
title: Run SAP PCM Console Job
description: Führt einen SAP-PCM-Konsolenjob aus einem PlaidCloud-Workflow-Schritt aus, um Stapelverarbeitung und administrative Vorgänge aus der Ferne auszuführen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-console-job.md
---

## Beschreibung



Startet einen Job in der SAP-PCM-Konsole auf dem entfernten PCM-Server – typischerweise für administrative oder Stapelaufgaben, die PCM über seine Konsolenschnittstelle statt über die Modellberechnungs-API bereitstellt.

Anwendungsfälle sind Archivierungsvorgänge, Hyperloader-Ausführungen oder herstellerspezifische Wartungsroutinen. Der genaue Job und seine Parameter hängen von Ihrer PCM-Bereitstellung ab.


## Unsere Referenzen


PlaidCloud ist ein offizieller SAP-Partner und bevorzugter Dienstleister für Services rund um Entwurf und Implementierung von SAP-PCM-Modellen.








## Beispiele


Wählen Sie in der Dropdown-Liste „Zu verwendender Agent“ aus, geben Sie den Pfad der Konsolendatei im Feld „Console File Path“ ein, aktivieren Sie bei Bedarf das Kontrollkästchen „Wait for Console Job to Complete“ und klicken Sie dann auf „Save and Run Step“.
