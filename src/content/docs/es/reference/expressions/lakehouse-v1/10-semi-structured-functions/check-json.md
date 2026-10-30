---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — Comprueba la validez de un documento JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

Comprueba la validez de un documento JSON.
Si la cadena de entrada es un documento JSON válido o un `NULL`, el resultado es `NULL`.
Si la entrada no puede traducirse a un valor JSON válido, la cadena de salida contiene el mensaje de error.

## Sintaxis de Analyze

```python
func.check_json(<expr>)
```

## Ejemplos de Analyze

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## Sintaxis SQL

```sql
CHECK_JSON( <expr> )
```

## Argumentos

| Argumentos | Descripción                      |
|------------|----------------------------------|
| `<expr>`   | Una expresión de tipo cadena     |

## Tipo de retorno

String

## Ejemplos de SQL

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
