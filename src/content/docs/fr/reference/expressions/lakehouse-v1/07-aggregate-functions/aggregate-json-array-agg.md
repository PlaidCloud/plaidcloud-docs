---
title: JSON_ARRAY_AGG (Lakehouse v1)
description: "JSON_ARRAY_AGG : convertit des valeurs en un tableau JSON en ignorant les NULL."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-array-agg.md
---

Convertit des valeurs en un tableau JSON en ignorant les NULL.

Voir aussi : [JSON_OBJECT_AGG](../aggregate-json-object-agg)

## Syntaxe Analyze

```python
func.json_array_agg(<expr>)
```

## Exemples Analyze
Consultez l'exemple SQL pour plus de détails.

## Syntaxe SQL

```sql
JSON_ARRAY_AGG(<expr>)
```

## Type de retour

Tableau JSON.

## Exemples

Cet exemple montre comment JSON_ARRAY_AGG agrège les valeurs de chaque colonne en tableaux JSON :

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
