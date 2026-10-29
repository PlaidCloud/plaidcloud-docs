---
title: PMOD (Lakehouse v2)
description: PMOD – gibt den positiven Modulo der Division zweier Zahlen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

Gibt den positiven Modulo der Division zweier Zahlen zurück.

## Analyze-Syntax

```python
func.pmod(<x>, <y>)
```

## Analyze-Beispiele

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## SQL-Syntax

```sql
PMOD(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
