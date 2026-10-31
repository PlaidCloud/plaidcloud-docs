---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — transforme chaque élément d'un tableau JSON à l'aide d'une expression Lambda donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

Transforme chaque élément d'un tableau JSON à l'aide d'une expression Lambda de transformation donnée. Pour en savoir plus sur les expressions Lambda, consultez Lambda Expressions.

## Syntaxe SQL

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## Alias

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## Type de retour

Tableau JSON.

## Exemples SQL

Dans cet exemple, chaque élément numérique du tableau est multiplié par 10, ce qui transforme le tableau d'origine en `[10, 20, 30, 40]` :

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
