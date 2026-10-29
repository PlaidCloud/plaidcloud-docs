---
title: DATE_SUB (Lakehouse v1)
description: DATE_SUB — odejmuje przedział czasu lub przedział dat od podanej daty lub daty z czasem (znacznik czasu/datetime).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-sub.md
---

Odejmuje przedział czasu lub przedział dat od podanej daty lub daty z czasem (znacznik czasu/datetime).

## Składnia Analyze

```python
func.date_sub(<unit>, <value>,  <date_or_time_expr>)
```

## Przykłady Analyze

```python
func.date_sub('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_sub('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2017-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
DATE_SUB(<unit>, <value>,  <date_or_time_expr>)
```
## Argumenty

| Argumenty             | Opis                                                                                                              |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Musi mieć jedną z następujących wartości: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` i `SECOND`          |
| `<value>`             | Liczba jednostek czasu, które chcesz odjąć. Na przykład aby odjąć 2 dni, wartość wynosi 2.                        |
| `<date_or_time_expr>` | Wartość typu `DATE` lub `TIMESTAMP`                                                                               |

## Zwracany typ

Funkcja zwraca wartość tego samego typu co argument `<date_or_time_expr>`.

## Przykłady SQL

```sql
SELECT date_sub(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_SUB(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2017-01-02                                        │
└───────────────────────────────────────────────────┘
```
