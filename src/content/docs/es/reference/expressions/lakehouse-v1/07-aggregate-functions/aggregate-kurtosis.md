---
title: KURTOSIS (Lakehouse v1)
description: "KURTOSIS: devuelve la curtosis en exceso (apuntamiento respecto a la distribución normal) de todos los valores de entrada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

Función de agregado.

La función `KURTOSIS()` devuelve la curtosis en exceso de todos los valores de entrada.

## Sintaxis de Analyze

```python
func.kurtosis(<expr>)
```

## Ejemplos de Analyze

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## Sintaxis de SQL

```sql
KURTOSIS(<expr>)
```

## Argumentos

| Argumentos | Descripción                     |
|-----------| -----------                     |
| `<expr>`  | Cualquier expresión numérica        |

## Tipo de valor devuelto

Float64 que admite valores NULL.

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
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

**Consulta de demostración: calcular la curtosis en exceso de los precios de las acciones de Apple**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**Resultado**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
