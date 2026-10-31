---
title: "AS_<type> (Lakehouse v1)"
description: AS_<type> — conversión estricta de valores VARIANT a otros tipos de datos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/as-type.md
---

Convierte de forma estricta valores `VARIANT` a otros tipos de datos.
Si el tipo de datos de entrada no es `VARIANT`, el resultado es `NULL`.
Si el tipo del valor dentro del `VARIANT` no coincide con el tipo de salida, el resultado es `NULL`.

## Sintaxis de Analyze
```python
func.as_boolean( <variant> )
func.as_integer( <variant> )
func.as_float( <variant> )
func.as_string( <variant> )
func.as_array( <variant> )
func.as_object( <variant> )
```

## Sintaxis SQL

```sql
AS_BOOLEAN( <variant> )
AS_INTEGER( <variant> )
AS_FLOAT( <variant> )
AS_STRING( <variant> )
AS_ARRAY( <variant> )
AS_OBJECT( <variant> )
```

## Argumentos

| Argumentos  | Descripción       |
|-------------|-------------------|
| `<variant>` | El valor VARIANT  |

## Tipo de retorno

- AS_BOOLEAN: BOOLEAN
- AS_INTEGER: BIGINT
- AS_FLOAT:   DOUBLE
- AS_STRING:  VARCHAR
- AS_ARRAY:   El VARIANT contiene un arreglo
- AS_OBJECT:  El VARIANT contiene un objeto

## Ejemplos de SQL

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
