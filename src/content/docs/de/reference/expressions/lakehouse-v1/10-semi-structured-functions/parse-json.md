---
title: PARSE_JSON (Lakehouse v1)
description: Interpretiert eine JSON-Eingabezeichenfolge und erzeugt einen VARIANT-Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json` und `try_parse_json` interpretieren eine Eingabezeichenfolge als JSON-Dokument und erzeugen einen VARIANT-Wert.

`try_parse_json` gibt einen NULL-Wert zurück, wenn beim Parsen ein Fehler auftritt.

## Analyze Syntax

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Analyze Examples

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

## SQL Syntax

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## Arguments

| Argumente | Beschreibung |
|-----------|--------------|
| `<expr>`  | Ein Ausdruck vom Typ Zeichenfolge (z. B. VARCHAR), der gültige JSON-Informationen enthält. |

## Return Type

VARIANT

## SQL Examples

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
