---
title: LOCATE (Lakehouse v2)
description: LOCATE — zwraca pozycję pierwszego wystąpienia podciągu w ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

Zwraca pozycję pierwszego wystąpienia podciągu w ciągu.

## Składnia Analyze

```python
func.locate(<substr>, <str>[, <pos>])
```

## Przykłady Analyze

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## Składnia SQL

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## Przykłady SQL

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
