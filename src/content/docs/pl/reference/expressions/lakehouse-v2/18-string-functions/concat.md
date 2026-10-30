---
title: CONCAT (Lakehouse v2)
description: CONCAT — łączy dwa lub więcej ciągów znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

Łączy dwa lub więcej ciągów znaków.

## Składnia Analyze

```python
func.concat(<str1>, <str2>[, ...])
```

## Przykłady Analyze

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## Składnia SQL

```sql
CONCAT(<str1>, <str2>[, ...])
```

## Przykłady SQL

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
