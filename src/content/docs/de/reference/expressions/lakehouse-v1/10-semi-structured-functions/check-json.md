---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — Prüft die Gültigkeit eines JSON-Dokuments.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

Prüft die Gültigkeit eines JSON-Dokuments.
Ist die Eingabezeichenfolge ein gültiges JSON-Dokument oder `NULL`, lautet die Ausgabe `NULL`.
Lässt sich die Eingabe nicht in einen gültigen JSON-Wert umwandeln, enthält die Ausgabezeichenfolge die Fehlermeldung.

## Analyze Syntax

```python
func.check_json(<expr>)
```

## Analyze Examples

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## SQL Syntax

```sql
CHECK_JSON( <expr> )
```

## Arguments

| Argumente | Beschreibung                    |
|-----------|---------------------------------|
| `<expr>`  | Ein Ausdruck vom Typ Zeichenfolge |

## Return Type

String

## SQL Examples

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```
