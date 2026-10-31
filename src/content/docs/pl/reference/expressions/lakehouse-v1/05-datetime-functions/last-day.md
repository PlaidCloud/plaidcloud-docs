---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY — zwraca ostatni dzień wskazanego przedziału (tygodnia, miesiąca, kwartału lub roku).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

Zwraca ostatni dzień wskazanego przedziału (tygodnia, miesiąca, kwartału lub roku) na podstawie podanej daty lub znacznika czasu.

## Składnia Analyze

```python
func.last_day(<date_expression>, <interval>)
```

## Przykłady Analyze

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
LAST_DAY(<date_expression>, <interval>)
```

| Parametr            | Opis                                                                                                              |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Wartość DATE lub TIMESTAMP, dla której obliczany jest ostatni dzień wskazanego przedziału.                        |
| `<interval>`        | Typ przedziału, dla którego należy znaleźć ostatni dzień. Akceptowane wartości to `week`, `month`, `quarter` i `year`. |

## Zwracany typ

Data.

## Przykłady SQL

Załóżmy, że chcesz ustalić datę rozliczenia, która zawsze przypada na ostatni dzień miesiąca, na podstawie dowolnej daty transakcji (np. 2024-11-13):

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
