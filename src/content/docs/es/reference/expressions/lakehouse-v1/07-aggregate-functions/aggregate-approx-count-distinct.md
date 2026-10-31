---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: "APPROX_COUNT_DISTINCT: estima el número de valores distintos de un conjunto de datos con el algoritmo HyperLogLog."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

Estima el número de valores distintos de un conjunto de datos con el algoritmo [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog). 

El algoritmo HyperLogLog proporciona una aproximación del número de elementos únicos con poca memoria y poco tiempo. Considere usar esta función con conjuntos de datos grandes cuando se pueda aceptar un resultado estimado. A cambio de cierta precisión, es un método rápido y eficiente para obtener recuentos distintos.

Para obtener un resultado exacto, use [COUNT_DISTINCT](../aggregate-count-distinct). Consulte los [ejemplos](#ejemplos-de-sql) para obtener más explicaciones.

## Sintaxis de Analyze

```python
func.approx_count_distinct(<expr>)
```

## Ejemplos de Analyze

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## Sintaxis de SQL

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## Tipo de valor devuelto

Entero.

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**Consulta de demostración: estimar el número de ID de usuario distintos**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**Resultado**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
