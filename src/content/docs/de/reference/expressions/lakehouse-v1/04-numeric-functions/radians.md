---
title: RADIANS (Lakehouse v1)
description: RADIANS – gibt das Argument x, von Grad ins Bogenmaß umgerechnet, zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

Gibt das Argument `x`, von Grad ins Bogenmaß umgerechnet, zurück.

## Analyze-Syntax

```python
func.radians( <x> )
```

## Analyze-Beispiele

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## SQL-Syntax

```sql
RADIANS( <x> )
```

## SQL-Beispiele

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
