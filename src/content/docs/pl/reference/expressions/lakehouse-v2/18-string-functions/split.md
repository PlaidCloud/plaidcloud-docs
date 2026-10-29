---
title: SPLIT (Lakehouse v2)
description: SPLIT — dzieli ciąg według ogranicznika i zwraca tablicę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

Dzieli ciąg według ogranicznika i zwraca tablicę.

## Składnia Analyze

```python
func.split(<str>, <delimiter>)
```

## Przykłady Analyze

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## Składnia SQL

```sql
SPLIT(<str>, <delimiter>)
```

## Przykłady SQL

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
