---
title: RADIANS (Lakehouse v2)
description: RADIANS — convertit des degrés en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

Convertit des degrés en radians.

## Syntaxe Analyze

```python
func.radians(<x>)
```

## Exemples Analyze

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## Syntaxe SQL

```sql
RADIANS(<x>)
```

## Exemples SQL

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
