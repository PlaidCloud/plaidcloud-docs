---
title: COSH (Lakehouse v2)
description: COSH – gibt den Kosinus hyperbolicus einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

Gibt den Kosinus hyperbolicus einer Zahl zurück.

## Analyze-Syntax

```python
func.cosh(<x>)
```

## Analyze-Beispiele

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL-Syntax

```sql
COSH(<x>)
```

## SQL-Beispiele

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
