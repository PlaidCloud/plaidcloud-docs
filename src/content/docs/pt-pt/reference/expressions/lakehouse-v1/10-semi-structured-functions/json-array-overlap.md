---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — verifica se existe alguma sobreposição entre duas matrizes JSON e devolve true se houver elementos comuns; caso contrário, devolve false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

Verifica se existe alguma sobreposição entre duas matrizes JSON e devolve `true` se houver elementos comuns; caso contrário, devolve `false`.

## Sintaxe SQL

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Tipo de retorno

A função devolve um valor booleano:

- `true` se existir pelo menos um elemento comum às duas matrizes JSON,
- `false` se não existirem elementos comuns.

## Exemplos de SQL

```sql
SELECT json_array_overlap(
    '["apple", "banana", "cherry"]'::JSON,  
    '["banana", "kiwi", "mango"]'::JSON
);

-[ RECORD 1 ]-----------------------------------
json_array_overlap('["apple", "banana", "cherry"]'::VARIANT, '["banana", "kiwi", "mango"]'::VARIANT): true


SELECT json_array_overlap(
    '["grape", "orange"]'::JSON,  
    '["apple", "kiwi"]'::JSON     
);

-[ RECORD 1 ]-----------------------------------
json_array_overlap('["grape", "orange"]'::VARIANT, '["apple", "kiwi"]'::VARIANT): false
```
