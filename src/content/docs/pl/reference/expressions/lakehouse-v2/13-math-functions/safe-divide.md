---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — funkcja PlaidCloud, która dzieli dwie liczby i zamiast zgłaszać błąd, gdy mianownik wynosi zero, zwraca wybraną przez Ciebie wartość.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

Funkcja PlaidCloud, dostępna w każdym silniku lakehouse. Dzieli pierwszą liczbę przez drugą. Gdy mianownik wynosi zero lub którakolwiek strona ma wartość NULL, wynikiem jest NULL, chyba że podano trzecią wartość, wtedy zwracana jest ta wartość. Obie strony są najpierw rzutowane na `DECIMAL(38, 10)`, dzięki czemu kolumny całkowitoliczbowe dzielą się bez obcinania.

## Składnia Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Przykłady Analyze

```python
func.safe_divide(table.revenue, table.units, 0)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | 0           |
| 100     | NULL  | 0           |
```

```python
func.safe_divide(table.revenue, table.units, None)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | NULL        |
```

## Odpowiednik SQL

Funkcja SQL o tej nazwie nie istnieje. Wyrażenie jest kompilowane do:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

Bez trzeciego argumentu nie ma funkcji COALESCE, a zerowy mianownik daje NULL:

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
