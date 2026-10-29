---
title: SINH (Lakehouse v2)
description: SINH – gibt den Sinus hyperbolicus einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

Gibt den Sinus hyperbolicus einer Zahl zurück.

## Analyze-Syntax

```python
func.sinh(<x>)
```

## Analyze-Beispiele

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL-Syntax

```sql
SINH(<x>)
```

## SQL-Beispiele

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
