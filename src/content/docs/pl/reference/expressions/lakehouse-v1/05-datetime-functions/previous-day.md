---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY — zwraca datę ostatniego wskazanego dnia tygodnia przed podaną datą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

Zwraca datę ostatniego wskazanego dnia tygodnia przed podaną datą lub znacznikiem czasu.

## Składnia Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Przykłady Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| Parametr            | Opis                                                                                                                                                                     |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Wartość `DATE` lub `TIMESTAMP`, od której obliczane jest poprzednie wystąpienie wskazanego dnia.                                                                          |
| `<target_day>`      | Docelowy dzień tygodnia, którego poprzednie wystąpienie należy znaleźć. Akceptowane wartości to `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` i `sunday`. |

## Zwracany typ

Data.

## Przykłady SQL

Aby znaleźć poprzedni piątek przed podaną datą, na przykład 2024-11-13:

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
