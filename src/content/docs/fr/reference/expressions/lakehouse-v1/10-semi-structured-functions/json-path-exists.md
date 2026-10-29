---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — vérifie si un chemin spécifié existe dans des données JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

Vérifie si un chemin spécifié existe dans des données JSON.

## Syntaxe Analyze

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Exemples Analyze

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## Syntaxe SQL

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data : indique les données JSON dans lesquelles effectuer la recherche. Il peut s'agir d'un objet JSON ou d'un tableau.

- json_path_expression : indique le chemin, à partir de la racine des données JSON représentée par `$`, que vous souhaitez vérifier dans les données JSON. Vous pouvez aussi inclure des conditions dans l'expression, en utilisant `@` pour désigner le nœud ou l'élément en cours d'évaluation, afin de filtrer les résultats.

## Type de retour

La fonction renvoie :

- `true` si le chemin JSON spécifié (et les conditions éventuelles) existe dans les données JSON.
- `false` si le chemin JSON spécifié (et les conditions éventuelles) n'existe pas dans les données JSON.
- NULL si json_data ou json_path_expression est NULL ou invalide.

## Exemples SQL

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
