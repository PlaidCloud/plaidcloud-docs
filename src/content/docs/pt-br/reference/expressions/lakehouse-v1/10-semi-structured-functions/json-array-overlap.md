---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — verifica se há sobreposição entre dois arrays JSON e retorna true se houver elementos em comum; caso contrário, retorna false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

Verifica se há sobreposição entre dois arrays JSON e retorna `true` se houver elementos em comum; caso contrário, retorna `false`.

## Sintaxe SQL

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Tipo de retorno

A função retorna um valor booleano:

- `true` se houver pelo menos um elemento em comum entre os dois arrays JSON,
- `false` se não houver elementos em comum.

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
