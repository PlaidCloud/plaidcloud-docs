---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: JSON_OBJECT_AGG — converte pares chave-valor num objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

Converte pares chave-valor num objeto JSON. Para cada linha de entrada, gera um par chave-valor em que a chave é obtida a partir de `<key_expression>` e o valor é obtido a partir de `<value_expression>`. Estes pares chave-valor são depois combinados num único objeto JSON.

Consulte também: [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Sintaxe do Analyze

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Exemplos do Analyze
Consulte o exemplo de SQL para obter mais detalhes

## Sintaxe SQL

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| Parâmetro        | Descrição                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | Especifica a chave do objeto JSON. **Só suporta expressões de cadeia de caracteres**. Se `key_expression` for avaliada como NULL, o par chave-valor é ignorado.  |
| value_expression | Especifica o valor do objeto JSON. Pode ser qualquer tipo de dados suportado. Se `value_expression` for avaliada como NULL, o par chave-valor é ignorado. |

## Tipo de retorno

Objeto JSON.

## Exemplos de SQL

Este exemplo demonstra como JSON_OBJECT_AGG pode ser utilizada para agregar diferentes tipos de dados — como decimais, inteiros, variantes JSON e matrizes — em objetos JSON, com a coluna b como chave de cada objeto JSON:

```sql
CREATE TABLE d (
    a DECIMAL(10, 2), 
    b STRING, 
    c INT, 
    d VARIANT, 
    e ARRAY(STRING)
);

INSERT INTO d VALUES
    (20, 'abc', NULL, '{"k":"v"}', ['a','b']),
    (10, 'de', 100, 'null', []),
    (4.23, NULL, 200, '"uvw"', ['x','y']),
    (5.99, 'xyz', 300, '[1,2,3]', ['z']);

SELECT
    json_object_agg(b, a) AS json_a,
    json_object_agg(b, c) AS json_c,
    json_object_agg(b, d) AS json_d,
    json_object_agg(b, e) AS json_e
FROM
    d;

-[ RECORD 1 ]-----------------------------------
json_a: {"abc":20.0,"de":10.0,"xyz":5.99}
json_c: {"de":100,"xyz":300}
json_d: {"abc":{"k":"v"},"de":null,"xyz":[1,2,3]}
json_e: {"abc":["a","b"],"de":[],"xyz":["z"]}
```
