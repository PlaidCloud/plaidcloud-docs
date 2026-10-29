---
title: PARSE_JSON (Lakehouse v1)
description: Interprète une chaîne JSON en entrée et produit une valeur VARIANT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json` et `try_parse_json` interprètent une chaîne en entrée comme un document JSON et produisent une valeur VARIANT.

`try_parse_json` renvoie une valeur NULL si une erreur se produit pendant l'analyse.

## Syntaxe Analyze

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Exemples Analyze

```python
func.parse_json('[-1, 12, 289, 2188, false]')

┌───────────────────────────────────────────────┐
│ func.parse_json('[-1, 12, 289, 2188, false]') │
├───────────────────────────────────────────────┤
│ [-1,12,289,2188,false]                        │
└───────────────────────────────────────────────┘

func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ')

┌──────────────────────────────────────────────────────────────┐
│ func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├──────────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                                 │
└──────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## Arguments

| Arguments | Description                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------|
| `<expr>`  | Une expression de type chaîne (par ex. VARCHAR) qui contient des informations JSON valides.       |

## Type de retour

VARIANT

## Exemples SQL

```sql
SELECT parse_json('[-1, 12, 289, 2188, false]');
┌──────────────────────────────────────────┐
│ parse_json('[-1, 12, 289, 2188, false]') │
├──────────────────────────────────────────┤
│ [-1,12,289,2188,false]                   │
└──────────────────────────────────────────┘

SELECT try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ');
┌─────────────────────────────────────────────────────────┐
│ try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├─────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                            │
└─────────────────────────────────────────────────────────┘
```
