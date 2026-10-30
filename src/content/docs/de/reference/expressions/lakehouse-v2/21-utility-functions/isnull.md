---
title: ISNULL (Lakehouse v2)
description: ISNULL — Prüft, ob ein Wert NULL ist. Gibt 1 zurück, wenn der Wert NULL ist, andernfalls 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

Prüft, ob ein Wert NULL ist. Gibt 1 zurück, wenn der Wert NULL ist, andernfalls 0.

## Analyze-Syntax

```python
func.isnull(<expr>)
```

## Analyze-Beispiele

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
ISNULL(<expr>)
```

## SQL-Beispiele

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
