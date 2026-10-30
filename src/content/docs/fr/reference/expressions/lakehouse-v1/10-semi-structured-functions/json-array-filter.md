---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — filtre les éléments d'un tableau JSON à partir d'une expression Lambda donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

Filtre les éléments d'un tableau JSON à partir d'une expression Lambda donnée, et ne renvoie que les éléments qui satisfont la condition. Pour en savoir plus sur les expressions Lambda, consultez Lambda Expressions.

## Syntaxe SQL

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Type de retour

Tableau JSON.

## Exemples SQL

Cet exemple filtre le tableau pour ne renvoyer que les chaînes commençant par la lettre `a`, ce qui donne `["apple", "avocado"]` :

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
