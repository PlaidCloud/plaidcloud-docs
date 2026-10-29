---
title: NEXT_DAY (Lakehouse v1)
description: NEXT_DAY — zwraca datę najbliższego wskazanego dnia tygodnia po podanej dacie lub znaczniku czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

Zwraca datę najbliższego wskazanego dnia tygodnia po podanej dacie lub znaczniku czasu.

## Składnia Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Przykłady Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| Parametr            | Opis                                                                                                                                                                     |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Wartość `DATE` lub `TIMESTAMP`, od której obliczane jest najbliższe wystąpienie wskazanego dnia.                                                                         |
| `<target_day>`      | Docelowy dzień tygodnia, którego najbliższe wystąpienie należy znaleźć. Akceptowane wartości to `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` i `sunday`. |

## Zwracany typ

Data.

## Przykłady SQL

Aby znaleźć najbliższy poniedziałek po określonej dacie, na przykład 2024-11-13:

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
