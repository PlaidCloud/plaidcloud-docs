---
title: RADIANS (Lakehouse v2)
description: RADIANS – wandelt Grad in Bogenmaß um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

Wandelt Grad in Bogenmaß um.

## Analyze-Syntax

```python
func.radians(<x>)
```

## Analyze-Beispiele

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## SQL-Syntax

```sql
RADIANS(<x>)
```

## SQL-Beispiele

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
