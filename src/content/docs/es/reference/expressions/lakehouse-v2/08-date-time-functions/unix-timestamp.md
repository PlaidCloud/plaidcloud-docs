---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — convierte un valor de fecha y hora en una marca de tiempo Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

Convierte un valor de fecha y hora en una marca de tiempo Unix.

## Sintaxis de Analyze

```python
func.unix_timestamp([<datetime>])
```

## Ejemplos de Analyze

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## Sintaxis de SQL

```sql
UNIX_TIMESTAMP([<datetime>])
```

## Ejemplos de SQL

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
