---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — zwraca liczbę znaków w ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

Zwraca liczbę znaków w ciągu.

## Składnia Analyze

```python
func.char_length(<str>)
```

## Przykłady Analyze

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## Składnia SQL

```sql
CHAR_LENGTH(<str>)
```

## Przykłady SQL

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
