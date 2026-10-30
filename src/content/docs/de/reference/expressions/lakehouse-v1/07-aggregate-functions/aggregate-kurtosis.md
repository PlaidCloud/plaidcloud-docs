---
title: KURTOSIS (Lakehouse v1)
description: KURTOSIS – gibt die Exzess-Kurtosis (Wölbung im Vergleich zur Normalverteilung) aller Eingabewerte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

Aggregatfunktion.

Die Funktion `KURTOSIS()` gibt die Exzess-Kurtosis aller Eingabewerte zurück.

## Analyze-Syntax

```python
func.kurtosis(<expr>)
```

## Analyze-Beispiele

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## SQL-Syntax

```sql
KURTOSIS(<expr>)
```

## Argumente

| Argumente | Beschreibung                    |
|-----------| -----------                     |
| `<expr>`  | Beliebiger numerischer Ausdruck |

## Rückgabetyp

Nullable Float64.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Exzess-Kurtosis für Apple-Aktienkurse berechnen**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**Ergebnis**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
