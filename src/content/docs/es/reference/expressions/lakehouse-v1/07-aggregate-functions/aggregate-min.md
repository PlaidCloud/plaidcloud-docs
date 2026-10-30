---
title: MIN (Lakehouse v1)
description: "MIN: devuelve el valor mínimo de un conjunto de valores."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

Función de agregado.

La función MIN() devuelve el valor mínimo de un conjunto de valores.

## Sintaxis de Analyze

```python
func.min(<column>)
```

## Ejemplos de Analyze

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## Sintaxis de SQL

```sql
MIN(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | Cualquier expresión |

## Tipo de valor devuelto

El valor mínimo, con el tipo del valor.

## Ejemplos de SQL

---
title: MIN
---

Función de agregado.

La función MIN() devuelve el valor mínimo de un conjunto de valores.

## Sintaxis de SQL

```sql
MIN(expression)
```

## Argumentos

| Argumentos   | Descripción |
| ----------- | ----------- |
| expression  | Cualquier expresión |

## Tipo de valor devuelto

El valor mínimo, con el tipo del valor.

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**Consulta de demostración: encontrar el precio mínimo de la gasolina de la estación 1**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**Resultado**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
