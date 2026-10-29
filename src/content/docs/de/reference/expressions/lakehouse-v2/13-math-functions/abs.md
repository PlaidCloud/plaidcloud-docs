---
title: ABS (Lakehouse v2)
description: ABS – gibt den Absolutwert einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

Gibt den Absolutwert einer Zahl zurück.

## Analyze-Syntax

```python
func.abs(<x>)
```

## Analyze-Beispiele

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## SQL-Syntax

```sql
ABS(<x>)
```

## SQL-Beispiele

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
