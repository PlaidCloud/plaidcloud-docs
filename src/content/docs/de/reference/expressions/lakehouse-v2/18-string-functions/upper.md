---
title: UPPER (Lakehouse v2)
description: UPPER — wandelt eine Zeichenfolge in Großbuchstaben um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

Wandelt eine Zeichenfolge in Großbuchstaben um.

## Analyze-Syntax

```python
func.upper(<str>)
```

## Analyze-Beispiele

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL-Syntax

```sql
UPPER(<str>)
```

## SQL-Beispiele

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
