---
title: TANH (Lakehouse v2)
description: TANH – gibt den Tangens hyperbolicus einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

Gibt den Tangens hyperbolicus einer Zahl zurück.

## Analyze-Syntax

```python
func.tanh(<x>)
```

## Analyze-Beispiele

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL-Syntax

```sql
TANH(<x>)
```

## SQL-Beispiele

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
