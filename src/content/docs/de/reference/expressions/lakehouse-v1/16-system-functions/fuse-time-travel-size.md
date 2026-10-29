---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE berechnet die Speichergröße historischer Daten (für Time Travel) von Tabellen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

Berechnet die Speichergröße historischer Daten (für Time Travel) von Tabellen.

## SQL-Syntax

```sql
-- Calculate historical data size for all tables in all databases
SELECT ...
FROM fuse_time_travel_size();

-- Calculate historical data size for all tables in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>');

-- Calculate historical data size for a specified table in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>', '<table_name>'));
```

## Ausgabe

Die Funktion gibt eine Ergebnismenge mit den folgenden Spalten zurück:

| Spalte                           | Beschreibung                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | Der Name der Datenbank, in der sich die Tabelle befindet.                                                  |
| `table_name`                     | Der Name der Tabelle.                                                                                |
| `is_dropped`                     | Gibt an, ob die Tabelle gelöscht wurde (`true` für gelöschte Tabellen, sonst `false`).          |
| `time_travel_size`               | Die gesamte Speichergröße der historischen Daten (für Time Travel) der Tabelle in Byte.                  |
| `latest_snapshot_size`           | Die Speichergröße des neuesten Snapshots der Tabelle in Byte.                                       |
| `data_retention_period_in_hours` | Die Aufbewahrungsdauer der Time-Travel-Daten in Stunden (`NULL` bedeutet, dass die Standard-Aufbewahrungsrichtlinie gilt). |
| `error`                          | Ein beim Abrufen der Speichergröße aufgetretener Fehler (`NULL`, wenn kein Fehler aufgetreten ist).               |

## SQL-Beispiele

Dieses Beispiel berechnet die historischen Daten aller Tabellen in der Datenbank `default`:

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
