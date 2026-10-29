---
title: Einen Bereich von Schritten in einem Workflow ausführen
description: Führen Sie einen bestimmten Bereich von Schritten in einem PlaidCloud-Workflow aus, um gezielt Teile Ihrer Datenverarbeitungs-Pipeline auszuführen.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

Das Ausführen einzelner Schritte ist nützlich, aber für Entwicklung, Tests oder Fehlersuche kann es auch sinnvoll sein, Teilmengen eines gesamten Workflows auszuführen. Um eine Teilmenge von Schritten auszuführen, wählen Sie alle Schritte aus, die Sie ausführen möchten, und wählen Sie im Menü **Aktionen** oben in der Schritthierarchie des Workflows **Ausgewählte(n) Schritt(e) ausführen**. Dadurch wird eine normale Workflow-Verarbeitung ausgelöst, die jedoch am Anfang der ausgewählten Schritte beginnt und endet, sobald der letzte ausgewählte Schritt abgeschlossen ist.

Befindet sich der letzte ausgewählte Schritt in einer Gruppe, die auf [**Parallel ausführen**](/de/guides/workflows/controlling-parallel-execution/) gesetzt ist, wartet die Ausführung außerdem, bis alle anderen ausgewählten Schritte dieser Gruppe abgeschlossen sind, bevor sie endet.
