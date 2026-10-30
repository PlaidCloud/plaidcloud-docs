---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION – gibt die Position des ersten Vorkommens eines Elements zurück (Zählung ab 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

Gibt die Position des ersten Vorkommens eines Elements zurück (Zählung ab 1).

## Analyze-Syntax

```python
func.array_position([10, 20, 30], 20)
```

## Analyze-Beispiele

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## SQL-Beispiele

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
