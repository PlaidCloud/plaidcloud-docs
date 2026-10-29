---
title: "AS_<type> (Lakehouse v1)"
description: AS_<type> — Strikte Umwandlung von VARIANT-Werten in andere Datentypen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/as-type.md
---

Wandelt `VARIANT`-Werte strikt in andere Datentypen um.
Ist der Eingabedatentyp nicht `VARIANT`, lautet die Ausgabe `NULL`.
Entspricht der Typ des Werts in der `VARIANT` nicht dem Ausgabetyp, lautet die Ausgabe `NULL`.

## Analyze Syntax
```python
func.as_boolean( <variant> )
func.as_integer( <variant> )
func.as_float( <variant> )
func.as_string( <variant> )
func.as_array( <variant> )
func.as_object( <variant> )
```

## SQL Syntax

```sql
AS_BOOLEAN( <variant> )
AS_INTEGER( <variant> )
AS_FLOAT( <variant> )
AS_STRING( <variant> )
AS_ARRAY( <variant> )
AS_OBJECT( <variant> )
```

## Arguments

| Argumente   | Beschreibung      |
|-------------|-------------------|
| `<variant>` | Der VARIANT-Wert  |

## Return Type

- AS_BOOLEAN: BOOLEAN
- AS_INTEGER: BIGINT
- AS_FLOAT:   DOUBLE
- AS_STRING:  VARCHAR
- AS_ARRAY:   Variant enthält ein Array
- AS_OBJECT:  Variant enthält ein Objekt

## SQL Examples

```sql
SELECT as_boolean(parse_json('true'));
┌────────────────────────────────┐
│ as_boolean(parse_json('true')) │
├────────────────────────────────┤
│ 1                              │
└────────────────────────────────┘

SELECT as_integer(parse_json('123'));
┌───────────────────────────────┐
│ as_integer(parse_json('123')) │
├───────────────────────────────┤
│ 123                           │
└───────────────────────────────┘

SELECT as_float(parse_json('12.34'));
┌───────────────────────────────┐
│ as_float(parse_json('12.34')) │
├───────────────────────────────┤
│ 12.34                         │
└───────────────────────────────┘

SELECT as_string(parse_json('"abc"'));
┌────────────────────────────────┐
│ as_string(parse_json('"abc"')) │
├────────────────────────────────┤
│ abc                            │
└────────────────────────────────┘

SELECT as_array(parse_json('[1,2,3]'));
┌─────────────────────────────────┐
│ as_array(parse_json('[1,2,3]')) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘

SELECT as_object(parse_json('{"k":"v","a":"b"}'));
┌────────────────────────────────────────────┐
│ as_object(parse_json('{"k":"v","a":"b"}')) │
├────────────────────────────────────────────┤
│ {"k":"v","a":"b"}                          │
└────────────────────────────────────────────┘

```
