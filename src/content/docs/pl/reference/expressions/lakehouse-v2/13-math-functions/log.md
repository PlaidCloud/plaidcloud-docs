---
title: LOG (Lakehouse v2)
description: LOG — zwraca logarytm liczby przy podanej podstawie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

Zwraca logarytm liczby przy podanej podstawie.

## Składnia Analyze

```python
func.log(<base>, <x>)
```

## Przykłady Analyze

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## Składnia SQL

```sql
LOG(<base>, <x>)
```

## Przykłady SQL

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
