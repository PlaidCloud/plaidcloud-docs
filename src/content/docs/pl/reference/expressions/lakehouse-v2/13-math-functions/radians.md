---
title: RADIANS (Lakehouse v2)
description: RADIANS — konwertuje stopnie na radiany.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

Konwertuje stopnie na radiany.

## Składnia Analyze

```python
func.radians(<x>)
```

## Przykłady Analyze

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## Składnia SQL

```sql
RADIANS(<x>)
```

## Przykłady SQL

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
