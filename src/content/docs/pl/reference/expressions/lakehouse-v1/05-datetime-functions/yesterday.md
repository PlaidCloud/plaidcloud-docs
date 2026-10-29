---
title: YESTERDAY (Lakehouse v1)
description: YESTERDAY — zwraca wczorajszą datę, tak samo jak today() - 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

Zwraca wczorajszą datę, tak samo jak `today() - 1`.

## Składnia Analyze

```python
func.yesterday()
```

## Przykłady Analyze

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## Składnia SQL

```sql
YESTERDAY()
```

## Typ zwracany

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
