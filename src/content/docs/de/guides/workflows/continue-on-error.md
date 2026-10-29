---
title: Bei Fehler fortfahren
description: Konfigurieren Sie PlaidCloud-Workflow-Schritte so, dass die Ausführung bei einem Fehler fortgesetzt wird und nachfolgende Schritte trotz früherer Fehler laufen.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

Workflow-Schritte können so eingestellt werden, dass die Verarbeitung auch bei einem Fehler fortgesetzt wird. Das kann bei Startbedingungen eines Workflows nützlich sein oder wenn Daten nur zeitweise verfügbar sind. Wenn der Schritt einen Fehler auslöst, wird dieser als Fehler protokolliert, der Workflow läuft aber weiter.



Um diese Option festzulegen, öffnen Sie das Formular des Schritts in der Workflow-Tabelle – klicken Sie auf sein Zahnradsymbol oder klicken Sie mit der rechten Maustaste darauf und wählen Sie **Schrittdetails bearbeiten** – und wechseln Sie zur Registerkarte **Allgemein**. Stellen Sie **Aktion bei einem Fehler** auf **Fortfahren**. Nach dem Speichern des aktualisierten Schritts führen Fehler dieses Schritts nicht mehr dazu, dass der Workflow anhält.



Schritte, die auf „Bei Fehler fortfahren“ gesetzt wurden, haben in der Hierarchietabelle der Workflow-Schritte eine besondere Kennzeichnung.
