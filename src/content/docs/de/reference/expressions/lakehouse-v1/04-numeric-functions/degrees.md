---
title: DEGREES (Lakehouse v1)
description: DEGREES – gibt das Argument x, vom Bogenmaß in Grad umgerechnet, zurück, wobei x im Bogenmaß angegeben wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

Gibt das Argument `x`, vom Bogenmaß in Grad umgerechnet, zurück, wobei `x` im Bogenmaß angegeben wird.

## Analyze-Syntax

```python
func.degrees( <x> )
```

## Analyze-Beispiele

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
DEGREES( <x> )
```

## SQL-Beispiele

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
