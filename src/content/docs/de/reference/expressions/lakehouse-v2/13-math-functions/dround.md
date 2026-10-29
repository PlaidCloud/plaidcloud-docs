---
title: DROUND (Lakehouse v2)
description: DROUND – Alias für `ROUND`. Siehe [ROUND](../round/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

Alias für `ROUND`. Siehe [ROUND](../round/).

## Analyze-Syntax

```python
func.dround(3.14159, 2)
```

## Analyze-Beispiele

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## SQL-Syntax

```sql
DROUND(<x>)
```

## SQL-Beispiele

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
