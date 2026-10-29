---
title: LCASE (Lakehouse v2)
description: LCASE — wandelt eine Zeichenfolge in Kleinbuchstaben um. Alias für `LOWER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

Wandelt eine Zeichenfolge in Kleinbuchstaben um. Alias für `LOWER`.

## Analyze-Syntax

```python
func.lcase(<str>)
```

## Analyze-Beispiele

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL-Syntax

```sql
LCASE(<str>)
```

## SQL-Beispiele

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
