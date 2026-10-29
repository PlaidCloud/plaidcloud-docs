---
title: DEGREES (Lakehouse v2)
description: DEGREES — convertit des radians en degrés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

Convertit des radians en degrés.

## Syntaxe Analyze

```python
func.degrees(<x>)
```

## Exemples Analyze

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## Syntaxe SQL

```sql
DEGREES(<x>)
```

## Exemples SQL

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
