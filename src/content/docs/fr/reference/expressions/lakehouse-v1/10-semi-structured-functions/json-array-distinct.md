---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — supprime les éléments en double d'un tableau JSON et renvoie un tableau ne contenant que des éléments distincts.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

Supprime les éléments en double d'un tableau JSON et renvoie un tableau ne contenant que des éléments distincts.

## Syntaxe SQL

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## Type de retour

Tableau JSON.

## Exemples SQL

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
