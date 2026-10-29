---
title: Table Restore to Timestamp (Schritt)
description: Stellen Sie eine PlaidCloud-Tabelle als Workflow-Schritt direkt auf ihren neuesten Snapshot zurück, der zu oder vor einem Zeitpunkt erstellt wurde.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## Beschreibung

**Tabelle: Auf Zeitstempel zurücksetzen** ersetzt eine Tabelle direkt durch ihren neuesten Snapshot, der zu oder vor einem Zeitpunkt erstellt wurde. Verwenden Sie den Schritt, um eine Tabelle auf den Stand eines Periodenendes oder vor einen fehlgeschlagenen Ladevorgang zurückzusetzen. Die Wiederherstellung ändert die Tabelle selbst, sodass jeder Schritt und jedes Dashboard, das sie liest, die wiederhergestellten Zeilen sieht.

## Auf einen Zeitpunkt zurücksetzen

| Einstellung | Erforderlich | Wirkung |
| --- | --- | --- |
| Tabelle | Ja | Die Tabelle, die wiederhergestellt wird. |
| Zeitstempel | Ja | Der Zeitpunkt, als ISO-8601-Zeit wie `2026-09-30T23:59:59Z` oder als Sekunden seit 1970. Eine Zeit ohne Zone gilt als UTC. Eine Workflow-Variable wie `{restore_time}` funktioniert ebenfalls. |
| Ein genau zum Zeitstempel erstellter Snapshot zählt | Nein | Standardmäßig aktiviert. Deaktivieren Sie die Option, um nur auf einen Snapshot zurückzusetzen, der vor dem Zeitstempel erstellt wurde. |

Wurde zu oder vor dem Zeitstempel kein Snapshot erstellt, endet der Schritt mit einer Warnung, lässt die Tabelle unverändert, und der Workflow wird fortgesetzt. Auch eine nicht gefundene Tabelle endet mit einer Warnung. Bei einer Speicher-Engine, die nur benannte Snapshots vorhält, kann die Tabelle nur auf einen Snapshot zurückgesetzt werden, der genau zum Zeitstempel erstellt wurde; erstellen Sie einen benannten Snapshot zu dem Zeitpunkt, zu dem Sie zurückkehren möchten.

## Verwandte Themen

- [Tabellen wiederherstellen](/de/reference/workflow-steps/import/restore-tables/)
- [Tabellenschritte](/de/reference/workflow-steps/tables/)
