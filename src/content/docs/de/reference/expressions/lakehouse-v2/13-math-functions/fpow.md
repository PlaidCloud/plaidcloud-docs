---
title: FPOW (Lakehouse v2)
description: FPOW – Alias für `POW`. Siehe [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

Alias für `POW`. Siehe [POW](../pow/).

## Analyze-Syntax

```python
func.fpow(2, 10)
```

## Analyze-Beispiele

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL-Syntax

```sql
FPOW(<x>)
```

## SQL-Beispiele

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
