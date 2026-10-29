---
title: Calculate PCM Model
description: Löst SAP-PCM-Modellberechnungen aus einem PlaidCloud-Workflow-Schritt aus, um Verarbeitungsjobs für Profitabilität und Kostenumlage auszuführen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## Beschreibung



Löst die Berechnungs-Engine in einem SAP-Profitability-and-Cost-Management-(PCM-)Modell aus. Verwenden Sie dies in einem Workflow, um die Kostenberechnung auszuführen, nachdem vorgelagerte Datenladevorgänge die Eingaben des Modells (Zuordnungen, Treiber, Quelldaten) befüllt haben.

Die Berechnung läuft auf der PCM-Serverseite asynchron; kombinieren Sie sie mit [Stop PCM Model Calculation](/de/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/), wenn Sie eine lang laufende Berechnung abbrechen müssen.


## Unsere Referenzen


PlaidCloud ist ein offizieller SAP-Partner und bevorzugter Dienstleister für Services rund um Entwurf und Implementierung von SAP-PCM-Modellen.







## Beispiele


Wählen Sie in der Dropdown-Liste „Zu verwendender Agent“ aus, geben Sie den Modellnamen im Feld „Model Name“ ein, aktivieren Sie bei Bedarf das Kontrollkästchen „Wait for Calculation to Complete“ und klicken Sie dann auf „Save and Run Step“.
