---
title: UCASE (Lakehouse v2)
description: UCASE — wandelt eine Zeichenfolge in Großbuchstaben um. Alias für `UPPER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

Wandelt eine Zeichenfolge in Großbuchstaben um. Alias für `UPPER`.

## Analyze-Syntax

```python
func.ucase(<str>)
```

## Analyze-Beispiele

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL-Syntax

```sql
UCASE(<str>)
```

## SQL-Beispiele

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
