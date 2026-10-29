---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — extrait la valeur d'un VARIANT contenant un OBJECT à partir de field_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

Extrait la valeur d'un `VARIANT` contenant un `OBJECT` à partir de field_name.
La valeur est renvoyée sous forme de `Variant`, ou `NULL` si l'un des arguments est `NULL`.

`GET_IGNORE_CASE` est similaire à `GET`, mais applique aux noms de champ une correspondance insensible à la casse.
La fonction recherche d'abord le nom de champ strictement identique ; s'il est introuvable, elle recherche le nom de champ sans tenir compte de la casse, dans l'ordre alphabétique (première correspondance).

## Syntaxe Analyze

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Exemples Analyze

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## Arguments

| Arguments      | Description                                                                     |
|----------------|---------------------------------------------------------------------------------|
| `<variant>`    | La valeur VARIANT contenant un ARRAY ou un OBJECT                               |
| `<field_name>` | La valeur de type chaîne qui indique la clé d'une paire clé-valeur de l'OBJECT  |

## Type de retour

VARIANT

## Exemples SQL

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
