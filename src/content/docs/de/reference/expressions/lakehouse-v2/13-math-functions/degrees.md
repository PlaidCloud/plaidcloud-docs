---
title: DEGREES (Lakehouse v2)
description: DEGREES – wandelt Bogenmaß in Grad um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

Wandelt Bogenmaß in Grad um.

## Analyze-Syntax

```python
func.degrees(<x>)
```

## Analyze-Beispiele

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## SQL-Syntax

```sql
DEGREES(<x>)
```

## SQL-Beispiele

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
