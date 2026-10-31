---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: "JSON_OBJECT_AGG : convertit des paires clé-valeur en un objet JSON."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

Convertit des paires clé-valeur en un objet JSON. Pour chaque ligne en entrée, elle génère une paire clé-valeur dont la clé provient de `<key_expression>` et la valeur de `<value_expression>`. Ces paires clé-valeur sont ensuite combinées en un seul objet JSON.

Voir aussi : [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Syntaxe Analyze

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Exemples Analyze
Consultez l'exemple SQL pour plus de détails.

## Syntaxe SQL

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| Paramètre        | Description                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | Spécifie la clé de l'objet JSON. **Seules les expressions de type chaîne sont prises en charge.** Si `key_expression` est évaluée à NULL, la paire clé-valeur est ignorée.  |
| value_expression | Spécifie la valeur de l'objet JSON. Elle peut être de n'importe quel type de données pris en charge. Si `value_expression` est évaluée à NULL, la paire clé-valeur est ignorée. |

## Type de retour

Objet JSON.

## Exemples SQL

Cet exemple montre comment JSON_OBJECT_AGG permet d'agréger différents types de données (décimaux, entiers, variantes JSON et tableaux) en objets JSON, la colonne b servant de clé pour chaque objet JSON :

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
