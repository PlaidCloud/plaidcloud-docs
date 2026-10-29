---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — Prüft, ob der Eingabewert ein JSON-Array ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

Prüft, ob der Eingabewert ein JSON-Array ist. Bitte beachten Sie, dass ein JSON-Array nicht dasselbe ist wie der Datentyp ARRAY. Ein JSON-Array ist eine in JSON häufig verwendete Datenstruktur, die eine geordnete Sammlung von Werten in eckigen Klammern `[ ]` darstellt. Es ist ein flexibles Format, um verschiedene Datentypen zu organisieren und auszutauschen, darunter Zeichenfolgen, Zahlen, Boolesche Werte, Objekte und Nullwerte.

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

## Analyze Syntax

```python
func.is_array(<expr>)
```

## Analyze Examples

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_ARRAY( <expr> )
```

## Return Type

Gibt `true` zurück, wenn der Eingabewert ein JSON-Array ist, andernfalls `false`.

## SQL Examples

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
