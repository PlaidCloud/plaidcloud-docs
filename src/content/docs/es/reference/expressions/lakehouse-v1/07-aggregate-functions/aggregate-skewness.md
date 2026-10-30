---
title: SKEWNESS (Lakehouse v1)
description: "SKEWNESS: devuelve la asimetría (asimetría de la distribución) de todos los valores de entrada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

Función de agregado.

La función `SKEWNESS()` devuelve la asimetría de todos los valores de entrada.

## Sintaxis de Analyze

```python
func.skewness(<expr>)
```

## Ejemplos de Analyze

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## Sintaxis de SQL

```sql
SKEWNESS(<expr>)
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
CREATE TABLE temperature_data (
                                  id INT,
                                  city_id INT,
                                  temperature FLOAT
);

INSERT INTO temperature_data (id, city_id, temperature)
VALUES (1, 1, 60),
       (2, 1, 65),
       (3, 1, 62),
       (4, 2, 70),
       (5, 2, 75);
```

**Consulta de demostración: calcular la asimetría de los datos de temperatura**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**Resultado**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
