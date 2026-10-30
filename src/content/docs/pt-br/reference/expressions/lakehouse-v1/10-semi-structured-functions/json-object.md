---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — Cria um objeto JSON a partir de chaves e valores alternados; TRY_JSON_OBJECT retorna NULL em vez de um erro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

Cria um objeto JSON a partir de argumentos alternados de chave e valor. As chaves devem ser strings; os valores podem ser constantes, expressões ou colunas. Um par cuja chave ou valor seja NULL é deixado de fora do resultado, ao contrário de JSON_ARRAY, que mantém um elemento NULL; use [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/) para mantê-los.

`TRY_JSON_OBJECT` recebe os mesmos argumentos e retorna NULL em vez de gerar um erro quando um argumento não pode ser convertido.

## Sintaxe do Analyze

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Exemplos do Analyze

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## Sintaxe SQL

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## Tipo de retorno

Objeto JSON.

## Exemplos de SQL

### Exemplos de SQL 1: criação de um objeto JSON com valores constantes

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### Exemplos de SQL 2: criação de objetos JSON a partir de dados da tabela

```sql
CREATE TABLE products (
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

INSERT INTO products (ProductName, Price)
VALUES
    ('Apple', 1.2),
    ('Banana', 0.5),
    ('Orange', 0.8);

SELECT JSON_OBJECT('name', ProductName, 'price', Price) FROM products;

json_object('name', productname, 'price', price)|
------------------------------------------------+
{"name":"Apple","price":1.2}                    |
{"name":"Banana","price":0.5}                   |
{"name":"Orange","price":0.8}                   |
```

### Exemplos de SQL 3: TRY_JSON_OBJECT retorna NULL em caso de erro

Um número ímpar de argumentos deixa uma chave sem valor, o que JSON_OBJECT rejeita:

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
