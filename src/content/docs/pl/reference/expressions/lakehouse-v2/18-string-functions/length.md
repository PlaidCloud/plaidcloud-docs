---
title: LENGTH (Lakehouse v2)
description: LENGTH — zwraca długość ciągu w bajtach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

Zwraca długość ciągu w bajtach.

## Składnia Analyze

```python
func.length(<str>)
```

## Przykłady Analyze

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## Składnia SQL

```sql
LENGTH(<str>)
```

## Przykłady SQL

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
