---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY – gibt das Produkt zweier Zahlen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

Gibt das Produkt zweier Zahlen zurück.

## Analyze-Syntax

```python
func.multiply(<x>, <y>)
```

## Analyze-Beispiele

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## SQL-Syntax

```sql
MULTIPLY(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
