---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — Extrahiert anhand von field_name einen Wert aus einer VARIANT, die ein OBJECT enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

Extrahiert anhand von field_name einen Wert aus einer `VARIANT`, die ein `OBJECT` enthält.
Der Wert wird als `Variant` zurückgegeben, oder als `NULL`, wenn eines der Argumente `NULL` ist.

`GET_IGNORE_CASE` ähnelt `GET`, ignoriert aber beim Abgleich der Feldnamen die Groß- und Kleinschreibung.
Zuerst wird nach dem exakt gleichen Feldnamen gesucht. Wird er nicht gefunden, erfolgt der Abgleich ohne Beachtung der Groß- und Kleinschreibung in alphabetischer Reihenfolge.

## Analyze Syntax

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Analyze Examples

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## Arguments

| Argumente      | Beschreibung                                                          |
|----------------|-----------------------------------------------------------------------|
| `<variant>`    | Der VARIANT-Wert, der entweder ein ARRAY oder ein OBJECT enthält      |
| `<field_name>` | Der Zeichenfolgenwert, der den Schlüssel eines Schlüssel-Wert-Paars im OBJECT angibt |

## Return Type

VARIANT

## SQL Examples

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
