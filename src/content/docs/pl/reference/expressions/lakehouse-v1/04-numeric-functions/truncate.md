---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE — zwraca liczbę x obciętą do d miejsc po przecinku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

Zwraca liczbę `x` obciętą do `d` miejsc po przecinku. Jeśli `d` wynosi 0, wynik nie zawiera przecinka ani części ułamkowej. Wartość `d` może być ujemna, co powoduje wyzerowanie `d` cyfr na lewo od przecinka w wartości `x`. Maksymalna wartość bezwzględna `d` wynosi 30; cyfry przekraczające 30 (lub -30) są obcinane.

## Składnia Analyze

```python
func.truncate( <x, d> )
```

## Przykłady Analyze

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Składnia SQL

```sql
TRUNCATE( <x, d> )
```

## Przykłady SQL

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
