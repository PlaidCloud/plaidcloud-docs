---
title: JSON_EACH (Lakehouse v1)
description: JSON_EACH — extrait les paires clé-valeur d'un objet JSON et décompose la structure en lignes distinctes dans le jeu de résultats.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-each.md
---

Extrait les paires clé-valeur d'un objet JSON et décompose la structure en lignes distinctes dans le jeu de résultats. Chaque ligne représente une paire clé-valeur distincte issue de l'expression JSON en entrée.

## Syntaxe Analyze

```python
func.json_each(<json_string>)
```

## Exemples Analyze

```python

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_each(func.parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                               │
│ ('grades','[90,85,92]')                                                                                    │
│ ('isStudent','false')                                                                                      │
│ ('name','"John"')                                                                                          │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
JSON_EACH(<json_string>)
```

## Type de retour

JSON_EACH renvoie un ensemble de tuples, chacun composé d'une clé de type STRING et de la valeur VARIANT correspondante.

## Exemples SQL

```sql
-- Extract key-value pairs from a JSON object representing information about a person
SELECT
  JSON_EACH(
    PARSE_JSON (
      '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
    )
  );


┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                     │
│ ('grades','[90,85,92]')                                                                          │
│ ('isStudent','false')                                                                            │
│ ('name','"John"')                                                                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Display data types of the extracted values
SELECT
  TYPEOF (
    JSON_EACH(
      PARSE_JSON (
        '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
      )
    )
  );

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ typeof(json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}'))) │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
