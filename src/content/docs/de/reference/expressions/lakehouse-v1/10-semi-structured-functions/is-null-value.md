---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — Prüft, ob der Eingabewert ein JSON-Null ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

Prüft, ob der Eingabewert ein JSON-`null` ist. Bitte beachten Sie, dass diese Funktion JSON-`null` prüft, nicht SQL-NULL. Um zu prüfen, ob ein Wert SQL-NULL ist, verwenden Sie [IS_NULL](../../03-conditional-functions/is-null).

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Analyze Syntax

```python
func.is_null_value(<expr>)
```

## Analyze Examples

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
IS_NULL_VALUE( <expr> )
```

## Return Type

Gibt `true` zurück, wenn der Eingabewert ein JSON-`null` ist, andernfalls `false`.

## SQL Examples

```sql
SELECT
  IS_NULL_VALUE(PARSE_JSON('{"name":"John", "age":null}') :age), --JSON null
  IS_NULL(NULL); --SQL NULL

┌──────────────────────────────────────────────────────────────────────────────┐
│ is_null_value(parse_json('{"name":"john", "age":null}'):age) │ is_null(null) │
├──────────────────────────────────────────────────────────────┼───────────────┤
│ true                                                         │ true          │
└──────────────────────────────────────────────────────────────────────────────┘
```
