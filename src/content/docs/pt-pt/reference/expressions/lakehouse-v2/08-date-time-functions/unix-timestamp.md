---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — converte um datetime num timestamp Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

Converte um datetime num timestamp Unix.

## Sintaxe de Analyze

```python
func.unix_timestamp([<datetime>])
```

## Exemplos de Analyze

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## Sintaxe SQL

```sql
UNIX_TIMESTAMP([<datetime>])
```

## Exemplos SQL

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
