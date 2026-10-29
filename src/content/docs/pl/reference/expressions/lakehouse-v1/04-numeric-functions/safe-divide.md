---
title: SAFE_DIVIDE (Lakehouse v1)
description: SAFE_DIVIDE — funkcja PlaidCloud, która dzieli dwie liczby i zamiast zgłaszać błąd zwraca wybraną przez Ciebie wartość, gdy dzielnik wynosi zero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

Funkcja PlaidCloud dostępna w każdym silniku lakehouse. Dzieli pierwszą liczbę przez drugą. Gdy dzielnik wynosi zero lub którakolwiek strona ma wartość NULL, wynikiem jest trzecia wartość; przekaż `None`, aby uzyskać NULL. W Lakehouse v1 wymagane są wszystkie trzy argumenty. Obie strony są najpierw rzutowane na `DECIMAL(38, 10)`, dzięki czemu kolumny całkowitoliczbowe dzielą się bez obcinania.

## Składnia Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
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

Nie istnieje funkcja SQL o tej nazwie. Wyrażenie jest kompilowane do:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```
