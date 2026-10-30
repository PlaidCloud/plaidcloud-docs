---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — Vérifie si la valeur en entrée est un tableau JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

Vérifie si la valeur en entrée est un tableau JSON. À noter : un tableau JSON n'est pas la même chose que le type de données ARRAY. Un tableau JSON est une structure de données courante en JSON, qui représente une collection ordonnée de valeurs placées entre crochets `[ ]`. C'est un format souple pour organiser et échanger des types de données variés, notamment des chaînes, des nombres, des booléens, des objets et des valeurs nulles. 

```json title='JSON Array Example:'
[
  "Apple",
  42,
  true,
  {"name": "John", "age": 30, "isStudent": false},
  [1, 2, 3],
  null
]
```

## Syntaxe Analyze

```python
func.is_array(<expr>)
```

## Exemples Analyze

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
IS_ARRAY( <expr> )
```

## Type de retour

Renvoie `true` si la valeur en entrée est un tableau JSON, et `false` dans le cas contraire.

## Exemples SQL

```sql
SELECT
  IS_ARRAY(PARSE_JSON('true')),
  IS_ARRAY(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_array(parse_json('true')) │ is_array(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ false                        │ true                            │
└────────────────────────────────────────────────────────────────┘
```
