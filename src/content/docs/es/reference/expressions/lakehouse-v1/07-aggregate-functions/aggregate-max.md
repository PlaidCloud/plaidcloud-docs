---
title: MAX (Lakehouse v1)
description: "MAX: devuelve el valor máximo de un conjunto de valores."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

Función de agregado.

La función MAX() devuelve el valor máximo de un conjunto de valores.

## Sintaxis de Analyze

```python
func.max(<column>)
```

## Ejemplos de Analyze

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## Sintaxis de SQL

```sql
MAX(<expr>)
```

## Argumentos

| Argumentos | Descripción |
|-----------| ----------- |
| `<expr>`  | Cualquier expresión |

## Tipo de valor devuelto

El valor máximo, con el tipo del valor.

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**Consulta de demostración: encontrar la temperatura máxima de la ciudad de Nueva York**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**Resultado**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
