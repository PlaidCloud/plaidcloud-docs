---
title: Stop PCM Model Calculation (Schritt)
description: Beenden Sie eine laufende SAP-PCM-Modellberechnung aus einem PlaidCloud-Workflow-Schritt, um die Verarbeitung bei Fehlern oder Problemen anzuhalten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation.md
---

## Beschreibung



Bricht eine laufende SAP-PCM-Modellberechnung ab. Nützlich, wenn eine Berechnung zu lange dauert, mit fehlerhaften Eingabedaten gestartet wurde oder gestoppt werden muss, um Serverressourcen für einen höher priorisierten Job freizugeben.

Wenn gerade keine Berechnung läuft, schreibt der Schritt eine Warnung in das Workflow-Protokoll und läuft weiter.


## Unsere Zertifizierungen


PlaidCloud ist ein offizieller SAP-Partner und ein bevorzugter Anbieter von Services rund um Design und Implementierung von SAP-PCM-Modellen.




## Beispiele


Wählen Sie in der Dropdown-Liste den **Zu verwendender Agent** aus, geben Sie den „Model Name“ ein, aktivieren Sie das Kontrollkästchen „Wait for Copy to Complete“ und klicken Sie dann auf „Speichern und ausführen“.
