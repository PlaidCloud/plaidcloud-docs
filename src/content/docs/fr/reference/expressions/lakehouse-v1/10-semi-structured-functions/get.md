---
title: "GET (semi-structuré, Lakehouse v1)"
description: GET — extrait la valeur d'un Variant contenant un ARRAY à partir de son index, ou d'un Variant contenant un OBJECT à partir de field_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

Extrait la valeur d'un `Variant` contenant un `ARRAY` à partir de son `index`, ou d'un `Variant` contenant un `OBJECT` à partir de `field_name`.
La valeur est renvoyée sous forme de `Variant`, ou `NULL` si l'un des arguments est `NULL`.

`GET` applique à `field_name` une correspondance sensible à la casse. Pour une correspondance insensible à la casse, utilisez `GET_IGNORE_CASE`.

## Syntaxe Analyze

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Exemples Analyze

```python
func.get(func.parse_json('[2.71, 3.14]'), 0);
┌──────────────────────────────────────────────┐
│ func.get(func.parse_json('[2.71, 3.14]'), 0) │
├──────────────────────────────────────────────┤
│ 2.71                                         │
└──────────────────────────────────────────────┘


func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌─────────────────────────────────────────────────────────────┐
│ func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├─────────────────────────────────────────────────────────────┤
│ 1                                                           │
└─────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## Arguments

| Arguments      | Description                                                                    |
|----------------|--------------------------------------------------------------------------------|
| `<variant>`    | La valeur VARIANT contenant un ARRAY ou un OBJECT                              |
| `<index>`      | La valeur Uint32 qui indique la position de la valeur dans l'ARRAY             |
| `<field_name>` | La valeur de type chaîne qui indique la clé d'une paire clé-valeur de l'OBJECT |

## Type de retour

VARIANT

## Exemples SQL

```sql
SELECT get(parse_json('[2.71, 3.14]'), 0);
┌────────────────────────────────────┐
│ get(parse_json('[2.71, 3.14]'), 0) │
├────────────────────────────────────┤
│ 2.71                               │
└────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├───────────────────────────────────────────────────┤
│ 1                                                 │
└───────────────────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────┤
│ NULL                                              │
└───────────────────────────────────────────────────┘
```
