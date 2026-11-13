---
title: Workflow-Variablen verwalten
description: Verwalten Sie Workflow-Variablen in PlaidCloud, um dynamische Werte zu speichern und zwischen Schritten weiterzugeben – für flexible Datenverarbeitungslogik.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

PlaidCloud unterstützt Variablen sowohl im Projektbereich als auch im Workflow-Bereich. So können Sie projektweite Variablen festlegen oder Informationen einfach zwischen Workflows weitergeben. Die Variablen und ihre Werte zeigen Sie an, indem Sie in der Hierarchie **Workflows** auf das Variablensymbol klicken.



In der Variablentabelle können Sie die Variablen und ihre aktuellen Werte einsehen und die Werte bearbeiten. Außerdem können Sie neue Variablen hinzufügen oder vorhandene löschen.

## Integrierte Variablen

Schritteinstellungen und Ausdrücke können diese integrierten Variablen verwenden, ohne dass Sie sie definieren müssen:

| Variable | Wert |
|---|---|
| `{project}`, `{model}` | Die IDs von Projekt und Workflow, in dem der Schritt läuft. |
| `{cloud}` | Der Name des Workspace. |
| `{date}` | Die aktuelle UTC-Zeit der Ausführung in Langform, zum Beispiel `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | Derselbe Zeitpunkt nach ISO 8601, zum Beispiel `2026-11-12T22:49:56+00:00`. |

Verwenden Sie `{date_iso}`, wenn ein Ausdruck einen Teil des Datums auslesen muss. Die ersten 7 Zeichen ergeben den Monat (`2026-11`), die ersten 10 den Tag (`2026-11-12`). `{date_iso}` funktioniert überall dort, wo `{date}` funktioniert, auch in E-Mail-Vorlagen für Benachrichtigungen sowie in den Schritten Prognose, Parity und Solver.
