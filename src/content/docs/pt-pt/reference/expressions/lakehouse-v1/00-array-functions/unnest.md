---
title: UNNEST (Lakehouse v1)
description: UNNEST — desagrega a matriz e devolve o conjunto de elementos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

Desagrega a matriz e devolve o conjunto de elementos.

## Sintaxe do Analyze

```python
func.unnest( <array> )
```

## Exemplos do Analyze

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
UNNEST( <array> )
```

## Exemplos SQL

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

## Um exemplo prático
Nos exemplos abaixo, utilizamos a seguinte tabela, chamada contacts, com a coluna phones definida como uma matriz de texto.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

A coluna phones é uma matriz unidimensional que contém os vários números de telefone que um contacto pode ter.

Para definir uma matriz multidimensional, acrescente os parênteses retos.

Por exemplo, pode definir uma matriz bidimensional da seguinte forma:

```python
column_name data_type [][]
```

Um exemplo de inserção de dados nessa tabela
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
ou
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

A função unnest() expande uma matriz numa lista de linhas. Por exemplo, a consulta seguinte expande todos os números de telefone da matriz phones.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Resultado:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
