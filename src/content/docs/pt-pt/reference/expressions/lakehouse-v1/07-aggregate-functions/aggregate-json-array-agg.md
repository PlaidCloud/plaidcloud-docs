---
title: JSON_ARRAY_AGG (Lakehouse v1)
description: JSON_ARRAY_AGG — converte valores numa matriz JSON, ignorando os NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-array-agg.md
---

Converte valores numa matriz JSON, ignorando os NULL.

Consulte também: [JSON_OBJECT_AGG](../aggregate-json-object-agg)

## Sintaxe do Analyze

```python
func.json_array_agg(<expr>)
```

## Exemplos do Analyze
Consulte o exemplo de SQL para obter mais detalhes

## Sintaxe SQL

```sql
JSON_ARRAY_AGG(<expr>)
```

## Tipo de retorno

Matriz JSON.

## Exemplos

Este exemplo demonstra como JSON_ARRAY_AGG agrega os valores de cada coluna em matrizes JSON:

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
    json_array_agg(a) AS aggregated_a, 
    json_array_agg(b) AS aggregated_b, 
    json_array_agg(c) AS aggregated_c, 
    json_array_agg(d) AS aggregated_d, 
    json_array_agg(e) AS aggregated_e
FROM d;

-[ RECORD 1 ]-----------------------------------
aggregated_a: [20.0,10.0,4.23,5.99]
aggregated_b: ["abc","de","xyz"]
aggregated_c: [100,200,300]
aggregated_d: [{"k":"v"},null,"uvw",[1,2,3]]
aggregated_e: [["a","b"],[],["x","y"],["z"]]
```
