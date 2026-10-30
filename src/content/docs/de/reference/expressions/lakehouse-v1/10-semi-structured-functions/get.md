---
title: "GET (Semi-Structured, Lakehouse v1)"
description: GET — Extrahiert einen Wert aus einer Variant, die ein ARRAY enthält, anhand des Index, oder aus einer Variant mit OBJECT anhand des Feldnamens.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

Extrahiert einen Wert aus einer `Variant`, die ein `ARRAY` enthält, anhand von `index`, oder aus einer `Variant`, die ein `OBJECT` enthält, anhand von `field_name`.
Der Wert wird als `Variant` zurückgegeben, oder als `NULL`, wenn eines der Argumente `NULL` ist.

`GET` beachtet beim Abgleich von `field_name` die Groß- und Kleinschreibung. Für einen Abgleich ohne Beachtung der Groß- und Kleinschreibung verwenden Sie `GET_IGNORE_CASE`.

## Analyze Syntax

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Analyze Examples

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

## SQL Syntax

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## Arguments

| Argumente      | Beschreibung                                                          |
|----------------|-----------------------------------------------------------------------|
| `<variant>`    | Der VARIANT-Wert, der entweder ein ARRAY oder ein OBJECT enthält      |
| `<index>`      | Der Uint32-Wert, der die Position des Werts im ARRAY angibt           |
| `<field_name>` | Der Zeichenfolgenwert, der den Schlüssel eines Schlüssel-Wert-Paars im OBJECT angibt |

## Return Type

VARIANT

## SQL Examples

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
