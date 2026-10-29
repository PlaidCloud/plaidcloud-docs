---
title: FLOOR (Lakehouse v2)
description: FLOOR – gibt die größte Ganzzahl zurück, die kleiner oder gleich einer Zahl ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

Gibt die größte Ganzzahl zurück, die kleiner oder gleich einer Zahl ist.

## Analyze-Syntax

```python
func.floor(<x>)
```

## Analyze-Beispiele

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## SQL-Syntax

```sql
FLOOR(<x>)
```

## SQL-Beispiele

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
