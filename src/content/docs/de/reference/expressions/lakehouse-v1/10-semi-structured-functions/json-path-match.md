---
title: JSON_PATH_MATCH (Lakehouse v1)
description: JSON_PATH_MATCH — Prüft, ob ein angegebener JSON-Pfadausdruck bestimmte Bedingungen erfüllt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-match.md
---

Prüft, ob ein angegebener JSON-Pfadausdruck bestimmte Bedingungen in JSON-Daten erfüllt. Bitte beachten Sie, dass der Operator `@@` ein Synonym für diese Funktion ist. Weitere Informationen finden Sie unter JSON Operators.


## Analyze Syntax

```python
func.json_path_match(<json_data>, <json_path_expression)
```

## Analyze Examples

```python
func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1')
┌──────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├──────────────────────────────────────────────────────────────────────────┤
│ true                                                                     │
└──────────────────────────────────────────────────────────────────────────┘

func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1')
┌────────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├────────────────────────────────────────────────────────────────────────────┤
│ false                                                                      │
└────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
JSON_PATH_MATCH(<json_data>, <json_path_expression>)
```

- `json_data`: Gibt die JSON-Daten an, die Sie untersuchen möchten. Es kann ein JSON-Objekt oder ein Array sein.
- `json_path_expression`: Gibt die Bedingungen an, die in den JSON-Daten geprüft werden. Dieser Ausdruck beschreibt den konkreten Pfad oder die Kriterien, auf die geprüft wird, etwa ob bestimmte Feldwerte in der JSON-Struktur bestimmte Bedingungen erfüllen. Das Symbol `$` steht für die Wurzel der JSON-Daten. Es leitet den Pfadausdruck ein und bezeichnet das Objekt der obersten Ebene in der JSON-Struktur.

## Return Type

Die Funktion gibt Folgendes zurück:

- `true`, wenn der angegebene JSON-Pfadausdruck die Bedingungen in den JSON-Daten erfüllt.
- `false`, wenn der angegebene JSON-Pfadausdruck die Bedingungen in den JSON-Daten nicht erfüllt.
- NULL, wenn `json_data` oder `json_path_expression` NULL oder ungültig ist.

## SQL Examples

```sql
-- Check if the value at JSON path $.a is equal to 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1');

┌────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├────────────────────────────────────────────────────────────────┤
│ true                                                           │
└────────────────────────────────────────────────────────────────┘

-- Check if the first element in the array at JSON path $.b is greater than 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1');

┌──────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├──────────────────────────────────────────────────────────────────┤
│ false                                                            │
└──────────────────────────────────────────────────────────────────┘

-- Check if any element in the array at JSON path $.b
-- from the second one to the last are greater than or equal to 2
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2');

┌───────────────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2') │
├───────────────────────────────────────────────────────────────────────────┤
│ true                                                                      │
└───────────────────────────────────────────────────────────────────────────┘

-- NULL is returned if either the json_data or json_path_expression is NULL or invalid.
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), NULL);

┌──────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), null) │
├──────────────────────────────────────────────────────────┤
│ NULL                                                     │
└──────────────────────────────────────────────────────────┘

SELECT JSON_PATH_MATCH(NULL, '$.a == 1');

┌───────────────────────────────────┐
│ json_path_match(null, '$.a == 1') │
├───────────────────────────────────┤
│ NULL                              │
└───────────────────────────────────┘
```
