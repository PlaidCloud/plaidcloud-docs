---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — vérifie si la valeur en entrée est un null JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

Vérifie si la valeur en entrée est un `null` JSON. À noter : cette fonction examine le `null` JSON, et non le NULL SQL. Pour vérifier si une valeur est un NULL SQL, utilisez [IS_NULL](../../03-conditional-functions/is-null).

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Syntaxe Analyze

```python
func.is_null_value(<expr>)
```

## Exemples Analyze

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
IS_NULL_VALUE( <expr> )
```

## Type de retour

Renvoie `true` si la valeur en entrée est un `null` JSON, et `false` dans le cas contraire.

## Exemples SQL

```sql
SELECT
  IS_NULL_VALUE(PARSE_JSON('{"name":"John", "age":null}') :age), --JSON null
  IS_NULL(NULL); --SQL NULL

┌──────────────────────────────────────────────────────────────────────────────┐
│ is_null_value(parse_json('{"name":"john", "age":null}'):age) │ is_null(null) │
├──────────────────────────────────────────────────────────────┼───────────────┤
│ true                                                         │ true          │
└──────────────────────────────────────────────────────────────────────────────┘
```
