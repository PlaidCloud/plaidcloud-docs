---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — dzieli ciąg według ogranicznika i zwraca element o podanym indeksie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

Dzieli ciąg według ogranicznika i zwraca element o podanym indeksie.

## Składnia Analyze

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Przykłady Analyze

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## Składnia SQL

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## Przykłady SQL

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
