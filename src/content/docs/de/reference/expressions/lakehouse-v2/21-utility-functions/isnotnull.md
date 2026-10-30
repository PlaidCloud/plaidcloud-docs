---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL — prüft, ob ein Wert nicht NULL ist. Gibt 1 zurück, wenn der Wert nicht NULL ist, andernfalls 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

Prüft, ob ein Wert nicht NULL ist. Gibt 1 zurück, wenn der Wert nicht NULL ist, andernfalls 0.

## Analyze-Syntax

```python
func.isnotnull(<expr>)
```

## Analyze-Beispiele

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
ISNOTNULL(<expr>)
```

## SQL-Beispiele

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
