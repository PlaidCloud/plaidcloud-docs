---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD — dodaje przedział czasu lub przedział dat do podanej daty lub daty z czasem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

Dodaje przedział czasu lub przedział dat do podanej daty lub daty z czasem (znacznik czasu/datetime).

## Składnia Analyze

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Przykłady Analyze

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## Argumenty

| Argumenty             | Opis                                                                                                              |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Musi mieć jedną z następujących wartości: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` i `SECOND`          |
| `<value>`             | Liczba jednostek czasu, które chcesz dodać. Na przykład aby dodać 2 dni, wartość wynosi 2.                        |
| `<date_or_time_expr>` | Wartość typu `DATE` lub `TIMESTAMP`                                                                               |

## Zwracany typ

Funkcja zwraca wartość tego samego typu co argument `<date_or_time_expr>`.

## Przykłady SQL

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
