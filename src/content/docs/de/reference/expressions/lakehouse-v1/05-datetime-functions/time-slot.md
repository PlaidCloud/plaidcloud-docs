---
title: TIME_SLOT (Lakehouse v1)
description: TIME_SLOT – rundet die Uhrzeit auf die halbe Stunde.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

Rundet die Uhrzeit auf die halbe Stunde.

## Analyze-Syntax

```python
func.time_slot(<expr>)
```

## Analyze-Beispiele

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## SQL-Syntax

```sql
time_slot(<expr>)
```

## Argumente

| Argumente   | Beschreibung |
| ----------- | ----------- |
| `<expr>`    | Zeitstempel |

## Rückgabetyp

`TIMESTAMP`, wird im Format „YYYY-MM-DD hh:mm:ss.ffffff“ zurückgegeben.

## SQL-Beispiele

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
