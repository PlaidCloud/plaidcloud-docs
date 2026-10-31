---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — transforma cada elemento de un arreglo JSON mediante una expresión Lambda especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

Transforma cada elemento de un arreglo JSON mediante una expresión Lambda de transformación especificada. Para obtener más información sobre las expresiones Lambda, consulte Expresiones Lambda.

## Sintaxis SQL

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## Alias

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## Tipo de retorno

Arreglo JSON.

## Ejemplos de SQL

En este ejemplo, cada elemento numérico del arreglo se multiplica por 10, de modo que el arreglo original se transforma en `[10, 20, 30, 40]`:

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
