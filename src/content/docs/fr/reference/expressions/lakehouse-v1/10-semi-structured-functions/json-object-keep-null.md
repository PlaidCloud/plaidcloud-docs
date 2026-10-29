---
title: JSON_OBJECT_KEEP_NULL (Lakehouse v1)
description: JSON_OBJECT_KEEP_NULL — crée un objet JSON à partir de clés et de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keep-null.md
---

Crée un objet JSON à partir de clés et de valeurs.

- Les arguments sont zéro, une ou plusieurs paires clé-valeur (les clés sont des chaînes et les valeurs peuvent être de n'importe quel type).
- Si une clé est NULL, la paire clé-valeur est omise de l'objet obtenu. En revanche, si une valeur est NULL, la paire clé-valeur est conservée.
- Les clés doivent être distinctes les unes des autres, et leur ordre dans le JSON obtenu peut différer de l'ordre que vous avez indiqué.
- `TRY_JSON_OBJECT_KEEP_NULL` renvoie une valeur NULL si une erreur se produit lors de la construction de l'objet.

Voir aussi : JSON_OBJECT

## Syntaxe SQL

```sql
JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])
```

## Type de retour

Objet JSON.

## Exemples SQL

```sql
SELECT JSON_OBJECT_KEEP_NULL();
┌─────────────────────────┐
│ json_object_keep_null() │
├─────────────────────────┤
│ {}                      │
└─────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('a', 3.14, 'b', 'xx', 'c', NULL);
┌────────────────────────────────────────────────────────┐
│ json_object_keep_null('a', 3.14, 'b', 'xx', 'c', null) │
├────────────────────────────────────────────────────────┤
│ {"a":3.14,"b":"xx","c":null}                           │
└────────────────────────────────────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('fruits', ['apple', 'banana', 'orange'], 'vegetables', ['carrot', 'celery']);
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_object_keep_null('fruits', ['apple', 'banana', 'orange'], 'vegetables', ['carrot', 'celery']) │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"fruits":["apple","banana","orange"],"vegetables":["carrot","celery"]}                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('key');
  |
1 | SELECT JSON_OBJECT_KEEP_NULL('key')
  |        ^^^^^^^^^^^^^^^^^^ The number of keys and values must be equal while evaluating function `json_object_keep_null('key')`


SELECT TRY_JSON_OBJECT_KEEP_NULL('key');
┌──────────────────────────────────┐
│ try_json_object_keep_null('key') │
├──────────────────────────────────┤
│ NULL                             │
└──────────────────────────────────┘
```
