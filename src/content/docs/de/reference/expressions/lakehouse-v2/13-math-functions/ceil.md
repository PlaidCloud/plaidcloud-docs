---
title: CEIL (Lakehouse v2)
description: CEIL – gibt die kleinste Ganzzahl zurück, die größer oder gleich einer Zahl ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

Gibt die kleinste Ganzzahl zurück, die größer oder gleich einer Zahl ist.

## Analyze-Syntax

```python
func.ceil(<x>)
```

## Analyze-Beispiele

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL-Syntax

```sql
CEIL(<x>)
```

## SQL-Beispiele

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
