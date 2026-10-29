---
title: DATE_TRUNC (Lakehouse v1)
description: DATE_TRUNC — obcina wartość daty, godziny lub znacznika czasu do określonej precyzji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

Obcina wartość daty, godziny lub znacznika czasu do określonej precyzji. Na przykład po obcięciu `2022-07-07` do `MONTH` wynikiem będzie `2022-07-01`; po obcięciu `2022-07-07 01:01:01.123456` do `SECOND` wynikiem będzie `2022-07-07 01:01:01.000000`.

## Składnia Analyze

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Przykłady Analyze

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## Argumenty

| Argumenty             | Opis                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------|
| `<precision>`          | Musi mieć jedną z następujących wartości: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` i `SECOND` |
| `<date_or_time_expr>` | Wartość typu `DATE` lub `TIMESTAMP`                                                                  |

## Zwracany typ

Funkcja zwraca wartość tego samego typu co argument `<date_or_time_expr>`.

## Przykłady SQL

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
