---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — extrae un valor de un VARIANT que contiene un OBJECT a partir de field_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

Extrae un valor de un `VARIANT` que contiene un `OBJECT` a partir de field_name.
El valor se devuelve como `Variant`, o como `NULL` si alguno de los argumentos es `NULL`.

`GET_IGNORE_CASE` es similar a `GET`, pero aplica una coincidencia sin distinción entre mayúsculas y minúsculas a los nombres de campo.
Primero busca el nombre de campo exactamente igual; si no lo encuentra, busca el nombre de campo sin distinguir mayúsculas y minúsculas por orden alfabético.

## Sintaxis de Analyze

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Ejemplos de Analyze

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## Argumentos

| Argumentos     | Descripción                                                                  |
|----------------|------------------------------------------------------------------------------|
| `<variant>`    | El valor VARIANT que contiene un ARRAY o un OBJECT                           |
| `<field_name>` | El valor de tipo cadena que especifica la clave de un par clave-valor de OBJECT |

## Tipo de retorno

VARIANT

## Ejemplos de SQL

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
