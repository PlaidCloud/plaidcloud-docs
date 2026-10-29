---
title: LCASE (Lakehouse v2)
description: LCASE — zamienia ciąg na małe litery. Alias funkcji `LOWER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

Zamienia ciąg na małe litery. Alias funkcji `LOWER`.

## Składnia Analyze

```python
func.lcase(<str>)
```

## Przykłady Analyze

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Składnia SQL

```sql
LCASE(<str>)
```

## Przykłady SQL

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
