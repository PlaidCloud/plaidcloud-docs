---
title: IF (Lakehouse v2)
description: IF — zwraca jedną z dwóch wartości w zależności od tego, czy warunek ma wartość TRUE, czy FALSE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

Zwraca jedną z dwóch wartości w zależności od tego, czy warunek ma wartość TRUE, czy FALSE.

## Składnia Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Przykłady Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Składnia SQL

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## Przykłady SQL

```sql
SELECT name, IF(score >= 60, 'Pass', 'Fail') AS result FROM students;

┌─────────┬────────┐
│ name    │ result │
├─────────┼────────┤
│ Alice   │ Pass   │
│ Bob     │ Fail   │
│ Charlie │ Pass   │
└─────────┴────────┘
```
