---
title: TOMORROW (Lakehouse v1)
description: TOMORROW — zwraca jutrzejszą datę, tak samo jak today() + 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

Zwraca jutrzejszą datę, tak samo jak `today() + 1`.

## Składnia Analyze

```python
func.tomorrow()
```

## Przykłady Analyze

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## Składnia SQL

```sql
TOMORROW()
```

## Typ zwracany

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
