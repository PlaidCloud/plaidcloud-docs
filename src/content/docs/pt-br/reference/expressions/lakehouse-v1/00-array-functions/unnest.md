---
title: UNNEST (Lakehouse v1)
description: UNNEST desaninha o array e retorna o conjunto de elementos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

Desaninha o array e retorna o conjunto de elementos.

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

## Exemplos de SQL

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

## Um Exemplo Prático
Nos exemplos abaixo, usaremos a seguinte tabela chamada contacts, com a coluna phones definida como um array de texto.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

A coluna phones é um array unidimensional que armazena os vários números de telefone que um contato pode ter.

Para definir um array multidimensional, adicione os colchetes.

Por exemplo, você pode definir um array bidimensional da seguinte forma:

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

A função unnest() expande um array em uma lista de linhas. Por exemplo, a consulta a seguir expande todos os números de telefone do array phones.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Saída:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
