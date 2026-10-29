---
title: CEILING (Lakehouse v2)
description: CEILING – gibt die kleinste Ganzzahl zurück, die größer oder gleich einer Zahl ist. Alias für `CEIL`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

Gibt die kleinste Ganzzahl zurück, die größer oder gleich einer Zahl ist. Alias für `CEIL`.

## Analyze-Syntax

```python
func.ceiling(<x>)
```

## Analyze-Beispiele

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL-Syntax

```sql
CEILING(<x>)
```

## SQL-Beispiele

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
