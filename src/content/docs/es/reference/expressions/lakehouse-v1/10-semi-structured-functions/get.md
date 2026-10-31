---
title: "GET (Semi-Structured, Lakehouse v1)"
description: GET — extrae un valor de un Variant que contiene un ARRAY por índice, o de un Variant que contiene un OBJECT por nombre de campo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

Extrae un valor de un `Variant` que contiene un `ARRAY` por `index`, o de un `Variant` que contiene un `OBJECT` por `field_name`.
El valor se devuelve como `Variant`, o como `NULL` si alguno de los argumentos es `NULL`.

`GET` aplica una coincidencia que distingue entre mayúsculas y minúsculas a `field_name`. Para una coincidencia sin distinción entre mayúsculas y minúsculas, utilice `GET_IGNORE_CASE`.

## Sintaxis de Analyze

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Ejemplos de Analyze

```python
func.get(func.parse_json('[2.71, 3.14]'), 0);
┌──────────────────────────────────────────────┐
│ func.get(func.parse_json('[2.71, 3.14]'), 0) │
├──────────────────────────────────────────────┤
│ 2.71                                         │
└──────────────────────────────────────────────┘


func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌─────────────────────────────────────────────────────────────┐
│ func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├─────────────────────────────────────────────────────────────┤
│ 1                                                           │
└─────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## Argumentos

| Argumentos     | Descripción                                                                     |
|----------------|---------------------------------------------------------------------------------|
| `<variant>`    | El valor VARIANT que contiene un ARRAY o un OBJECT                              |
| `<index>`      | El valor Uint32 que especifica la posición del valor en el ARRAY                |
| `<field_name>` | El valor de tipo cadena que especifica la clave de un par clave-valor de OBJECT |

## Tipo de retorno

VARIANT

## Ejemplos de SQL

```sql
SELECT get(parse_json('[2.71, 3.14]'), 0);
┌────────────────────────────────────┐
│ get(parse_json('[2.71, 3.14]'), 0) │
├────────────────────────────────────┤
│ 2.71                               │
└────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├───────────────────────────────────────────────────┤
│ 1                                                 │
└───────────────────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────┤
│ NULL                                              │
└───────────────────────────────────────────────────┘
```
