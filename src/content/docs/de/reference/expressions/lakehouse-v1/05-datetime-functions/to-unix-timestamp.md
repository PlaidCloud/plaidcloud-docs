---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP – wandelt einen Timestamp in einem Datums-/Zeitformat in das Unix-Timestamp-Format um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

Wandelt einen Timestamp in einem Datums-/Zeitformat in das Unix-Timestamp-Format um. Ein Unix-Timestamp gibt die Anzahl der Sekunden an, die seit dem 1. Januar 1970, 00:00:00 UTC vergangen sind.

## Analyze-Syntax

```python
func.to_unix_timestamp(<expr>)
```

## Analyze-Beispiele

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## Argumente

| Argumente   | Beschreibung        |
| ----------- | ------------------- |
| `<expr>`    | Timestamp           |

Weitere Informationen zum Datentyp Timestamp finden Sie unter „Date & Time“.

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
