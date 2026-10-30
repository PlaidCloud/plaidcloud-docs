---
title: REGEXP_COUNT (Lakehouse v2)
description: "Użyj funkcji dopasowywania wzorców REGEXP_COUNT w PlaidCloud Lakehouse. Zwraca liczbę wystąpień wzorca wyrażenia regularnego w ciągu znaków."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

Zwraca liczbę wystąpień wzorca wyrażenia regularnego w ciągu znaków.

## Składnia Analyze

```python
func.regexp_count(<str>, <pattern>)
```

## Przykłady Analyze

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## Składnia SQL

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## Przykłady SQL

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
