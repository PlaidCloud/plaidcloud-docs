---
title: JQ (Lakehouse v1)
description: JQ — la fonction JQ est une fonction SQL renvoyant un ensemble de lignes, qui permet d'appliquer jq.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

La fonction JQ est une fonction SQL renvoyant un ensemble de lignes, qui permet d'appliquer des filtres [jq](https://jqlang.github.io/jq/) à des données JSON stockées dans des colonnes Variant. Avec cette fonction, vous pouvez traiter des données JSON en appliquant un filtre jq donné, et obtenir les résultats sous forme d'un ensemble de lignes.

## Syntaxe SQL

```sql
JQ (<jq_expression>, <json_data>)
```

| Paramètre       | Description                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jq_expression` | Une expression de filtre `jq` qui définit comment traiter et transformer les données JSON avec la syntaxe `jq`. Cette expression peut indiquer comment sélectionner, modifier et manipuler les données au sein d'objets et de tableaux JSON. Pour en savoir plus sur la syntaxe, les filtres et les fonctions pris en charge par jq, consultez le [manuel de jq](https://jqlang.github.io/jq/manual/#basic-filters). |
| `json_data`     | Les données en entrée au format JSON que vous souhaitez traiter ou transformer avec l'expression de filtre `jq`. Il peut s'agir d'un objet JSON, d'un tableau ou de toute structure de données JSON valide.                                                                                                                                                  |

## Type de retour

La fonction JQ renvoie un ensemble de valeurs JSON, chaque valeur correspondant à un élément du résultat transformé ou extrait selon `<jq_expression>`.

## Exemples SQL

Pour commencer, nous créons une table nommée `customer_data` avec des colonnes `id` et `profile`, où `profile` est de type JSON pour stocker les informations des utilisateurs :

```sql
CREATE TABLE customer_data (
    id INT,
    profile JSON
);

INSERT INTO customer_data VALUES
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 25, "city": "Los Angeles"}'),
    (3, '{"name": "Charlie", "age": 35, "city": "Chicago"}');
```

Cet exemple extrait des champs précis des données JSON :

```sql
SELECT
    id,
    jq('.name', profile) AS customer_name
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   customer_name   │
├─────────────────┼───────────────────┤
│               1 │ "Alice"           │
│               2 │ "Bob"             │
│               3 │ "Charlie"         │
└─────────────────────────────────────┘
```

Cet exemple sélectionne l'ID de chaque utilisateur et son âge augmenté de 1 :

```sql
SELECT
    id,
    jq('.age + 1', profile) AS updated_age
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │    updated_age    │
├─────────────────┼───────────────────┤
│               1 │ 31                │
│               2 │ 26                │
│               3 │ 36                │
└─────────────────────────────────────┘
```

Cet exemple convertit les noms de villes en majuscules :

```sql
SELECT
    id,
    jq('.city | ascii_upcase', profile) AS city_uppercase
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   city_uppercase  │
├─────────────────┼───────────────────┤
│               1 │ "NEW YORK"        │
│               2 │ "LOS ANGELES"     │
│               3 │ "CHICAGO"         │
└─────────────────────────────────────┘
```
