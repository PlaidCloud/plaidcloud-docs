---
title: PARSE_JSON (Lakehouse v1)
description: Interpretuje wejściowy ciąg JSON, tworząc wartość VARIANT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json` i `try_parse_json` interpretują wejściowy ciąg znaków jako dokument JSON, tworząc wartość VARIANT.

`try_parse_json` zwraca wartość NULL, jeśli podczas analizy wystąpi błąd.

## Składnia Analyze

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Przykłady Analyze

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

## Składnia SQL

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## Argumenty

| Argumenty | Opis                                                                           |
|-----------|--------------------------------------------------------------------------------|
| `<expr>`  | Wyrażenie typu ciąg znaków (np. VARCHAR) zawierające prawidłowe dane JSON.     |

## Typ zwracany

VARIANT

## Przykłady SQL

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
