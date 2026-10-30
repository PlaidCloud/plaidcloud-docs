---
title: RETENTION (Lakehouse v1)
description: "RETENTION: función de agregado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

Función de agregado

La función RETENTION() recibe como argumentos un conjunto de condiciones, de 1 a 32 argumentos de tipo UInt8, que indican si se cumplió una determinada condición para el evento.

Se puede especificar como argumento cualquier condición (como en WHERE).

Las condiciones, excepto la primera, se aplican por pares: el resultado de la segunda será verdadero si la primera y la segunda son verdaderas; el de la tercera, si la primera y la tercera son verdaderas, y así sucesivamente.

## Sintaxis de Analyze

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Ejemplos de Analyze

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## Sintaxis de SQL

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## Argumentos

| Argumentos | Descripción                                 |
|-----------|---------------------------------------------|
| `<cond>`  | Una expresión que devuelve un resultado booleano |

## Tipo de valor devuelto

La matriz de 1 o 0.

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**Consulta de demostración: calcular la retención de usuarios según los eventos de registro, inicio de sesión y compra**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**Resultado**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
