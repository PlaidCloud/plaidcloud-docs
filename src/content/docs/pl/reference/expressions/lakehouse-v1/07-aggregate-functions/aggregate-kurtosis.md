---
title: KURTOSIS (Lakehouse v1)
description: KURTOSIS — zwraca kurtozę nadmiarową (smukłość w porównaniu z rozkładem normalnym) wszystkich wartości wejściowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

Funkcja agregująca.

Funkcja `KURTOSIS()` zwraca kurtozę nadmiarową wszystkich wartości wejściowych.

## Składnia Analyze

```python
func.kurtosis(<expr>)
```

## Przykłady Analyze

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## Składnia SQL

```sql
KURTOSIS(<expr>)
```

## Argumenty

| Argumenty | Opis                            |
|-----------| -----------                     |
| `<expr>`  | Dowolne wyrażenie liczbowe      |

## Typ zwracany

Nullable Float64.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE stock_prices (
  id INT,
  stock_symbol VARCHAR,
  price FLOAT
);

INSERT INTO stock_prices (id, stock_symbol, price)
VALUES (1, 'AAPL', 150),
       (2, 'AAPL', 152),
       (3, 'AAPL', 148),
       (4, 'AAPL', 160),
       (5, 'AAPL', 155);
```

**Przykład zapytania: obliczenie kurtozy nadmiarowej dla cen akcji Apple**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**Wynik**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
