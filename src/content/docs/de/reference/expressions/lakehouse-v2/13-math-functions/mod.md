---
title: MOD (Lakehouse v2)
description: MOD – gibt den Rest der Division zweier Zahlen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

Gibt den Rest der Division zweier Zahlen zurück.

## Analyze-Syntax

```python
func.mod(<x>, <y>)
```

## Analyze-Beispiele

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
MOD(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
