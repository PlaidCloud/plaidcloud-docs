---
title: UNNEST (Lakehouse v1)
description: UNNEST — desanida el arreglo y devuelve el conjunto de elementos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

Desanida el arreglo y devuelve el conjunto de elementos.

## Sintaxis de Analyze

```python
func.unnest( <array> )
```

## Ejemplos de Analyze

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
UNNEST( <array> )
```

## Ejemplos de SQL

```sql
SELECT UNNEST([1, 2]);

┌─────────────────┐
│  unnest([1, 2]) │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘

-- UNNEST(array) can be used as a table function.
SELECT * FROM UNNEST([1, 2]);

┌─────────────────┐
│      value      │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘
```

## Un ejemplo práctico
En los ejemplos siguientes se usa la siguiente tabla llamada contacts, con la columna phones definida como un arreglo de texto.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

La columna phones es un arreglo unidimensional que contiene los distintos números de teléfono que puede tener un contacto.

Para definir un arreglo multidimensional, se añaden corchetes.

Por ejemplo, puede definir un arreglo bidimensional de la siguiente manera:

```python
column_name data_type [][]
```

Un ejemplo de inserción de datos en esa tabla
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
o
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

La función unnest() expande un arreglo en una lista de filas. Por ejemplo, la siguiente consulta expande todos los números de teléfono del arreglo phones.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Salida:
|    nombre    |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
