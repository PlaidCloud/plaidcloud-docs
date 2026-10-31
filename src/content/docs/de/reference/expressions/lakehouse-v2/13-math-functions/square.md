---
title: SQUARE (Lakehouse v2)
description: SQUARE – gibt das Quadrat einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

Gibt das Quadrat einer Zahl zurück.

## Analyze-Syntax

```python
func.square(<x>)
```

## Analyze-Beispiele

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## SQL-Syntax

```sql
SQUARE(<x>)
```

## SQL-Beispiele

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
