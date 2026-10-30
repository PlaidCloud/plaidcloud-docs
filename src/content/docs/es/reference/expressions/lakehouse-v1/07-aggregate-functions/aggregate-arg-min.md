---
title: ARG_MIN (Lakehouse v1)
description: "ARG_MIN: calcula el valor de arg correspondiente al valor mínimo de val."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

Calcula el valor de `arg` correspondiente al valor mínimo de `val`. Si hay varios valores distintos de `arg` para los valores mínimos de `val`, devuelve el primero de ellos que se encuentre.

## Sintaxis de Analyze

```python
func.arg_min(<expr>)
```

## Ejemplos de Analyze

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## Sintaxis de SQL

```sql
ARG_MIN(<arg>, <val>)
```

## Argumentos

| Argumentos | Descripción                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argumento de cualquier tipo de datos compatible con PlaidCloud Lakehouse |
| `<val>`   | Valor de cualquier tipo de datos compatible con PlaidCloud Lakehouse    |

## Tipo de valor devuelto

Valor de `arg` correspondiente al valor mínimo de `val`.

 coincide con el tipo de `arg`.

## Ejemplos de SQL

Cree una tabla students con las columnas id, name y score, e inserte algunos datos:
```sql
CREATE TABLE students (
  id INT,
  name VARCHAR,
  score INT
);

INSERT INTO students (id, name, score) VALUES
  (1, 'Alice', 80),
  (2, 'Bob', 75),
  (3, 'Charlie', 90),
  (4, 'Dave', 80);
```

Ahora puede usar ARG_MIN para encontrar el nombre del estudiante con la puntuación más baja:
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

Resultado:
```sql
| student_name |
|--------------|
| Charlie      |
```
