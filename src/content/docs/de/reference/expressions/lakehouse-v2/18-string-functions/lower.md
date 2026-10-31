---
title: LOWER (Lakehouse v2)
description: LOWER — wandelt eine Zeichenfolge in Kleinbuchstaben um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

Wandelt eine Zeichenfolge in Kleinbuchstaben um.

## Analyze-Syntax

```python
func.lower(<str>)
```

## Analyze-Beispiele

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL-Syntax

```sql
LOWER(<str>)
```

## SQL-Beispiele

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
