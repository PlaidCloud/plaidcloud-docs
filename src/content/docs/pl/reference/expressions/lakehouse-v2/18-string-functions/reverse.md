---
title: "REVERSE (tekst, Lakehouse v2)"
description: REVERSE — odwraca kolejność znaków w ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

Odwraca kolejność znaków w ciągu.

## Składnia Analyze

```python
func.reverse(<str>)
```

## Przykłady Analyze

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## Składnia SQL

```sql
REVERSE(<str>)
```

## Przykłady SQL

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
