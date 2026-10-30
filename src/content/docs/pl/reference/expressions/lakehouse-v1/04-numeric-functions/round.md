---
title: ROUND (Lakehouse v1)
description: ROUND — zaokrągla argument x do d miejsc po przecinku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

Zaokrągla argument x do d miejsc po przecinku. Algorytm zaokrąglania zależy od typu danych x. Jeśli d nie zostanie podane, domyślnie wynosi 0. Wartość d może być ujemna, co powoduje wyzerowanie d cyfr na lewo od przecinka w wartości x. Maksymalna wartość bezwzględna d wynosi 30; cyfry przekraczające 30 (lub -30) są obcinane.

Używając wyniku tej funkcji w obliczeniach, pamiętaj o potencjalnych problemach z precyzją wynikających z tego, że zwracanym typem danych jest DOUBLE, co może wpłynąć na ostateczną dokładność:

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Składnia Analyze

```python
func.round( <x, d> )
```

## Przykłady Analyze

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## Składnia SQL

```sql
ROUND( <x, d> )
```

## Przykłady SQL

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
