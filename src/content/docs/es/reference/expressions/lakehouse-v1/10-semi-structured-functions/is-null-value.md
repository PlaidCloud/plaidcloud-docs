---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — comprueba si el valor de entrada es un null de JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

Comprueba si el valor de entrada es un `null` de JSON. Tenga en cuenta que esta función examina el `null` de JSON, no el NULL de SQL. Para comprobar si un valor es NULL de SQL, utilice [IS_NULL](../../03-conditional-functions/is-null).

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Sintaxis de Analyze

```python
func.is_null_value(<expr>)
```

## Ejemplos de Analyze

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
IS_NULL_VALUE( <expr> )
```

## Tipo de retorno

Devuelve `true` si el valor de entrada es un `null` de JSON y `false` en caso contrario.

## Ejemplos de SQL

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
