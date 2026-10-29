---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — transforma cada elemento de um array JSON usando uma expressão Lambda especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

Transforma cada elemento de um array JSON usando uma expressão Lambda de transformação especificada. Para obter mais informações sobre expressões Lambda, consulte Expressões Lambda.

## Sintaxe SQL

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## Aliases

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## Tipo de retorno

Array JSON.

## Exemplos de SQL

Neste exemplo, cada elemento numérico do array é multiplicado por 10, transformando o array original em `[10, 20, 30, 40]`:

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
