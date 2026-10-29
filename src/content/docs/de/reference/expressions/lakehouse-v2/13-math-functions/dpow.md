---
title: DPOW (Lakehouse v2)
description: DPOW – Alias für `POW`. Siehe [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dpow.md
---

Alias für `POW`. Siehe [POW](../pow/).

## Analyze-Syntax

```python
func.dpow(2, 10)
```

## Analyze-Beispiele

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL-Syntax

```sql
DPOW(<x>)
```

## SQL-Beispiele

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
