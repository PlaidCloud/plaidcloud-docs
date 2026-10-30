---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT — gibt die letzten N Zeichen einer Zeichenfolge von rechts zurück. Alias für `RIGHT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

Gibt die letzten N Zeichen einer Zeichenfolge von rechts zurück. Alias für `RIGHT`.

## Analyze-Syntax

```python
func.strright(<str>, <len>)
```

## Analyze-Beispiele

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL-Syntax

```sql
STRRIGHT(<str>, <len>)
```

## SQL-Beispiele

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
