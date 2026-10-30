---
title: "GET (Semi-Structured, Lakehouse v1)"
description: GET — extrai o valor de um Variant que contém um ARRAY através do índice, ou de um Variant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

Extrai o valor de um `Variant` que contém um `ARRAY` através de `index`, ou de um `Variant` que contém um `OBJECT` através de `field_name`.
O valor é devolvido como `Variant` ou `NULL` se qualquer um dos argumentos for `NULL`.

`GET` aplica correspondência com distinção entre maiúsculas e minúsculas a `field_name`. Para correspondência sem distinção entre maiúsculas e minúsculas, utilize `GET_IGNORE_CASE`.

## Sintaxe do Analyze

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## Argumentos

| Argumentos     | Descrição                                                                |
|----------------|--------------------------------------------------------------------------|
| `<variant>`    | O valor VARIANT que contém um ARRAY ou um OBJECT                         |
| `<index>`      | O valor Uint32 que especifica a posição do valor no ARRAY                |
| `<field_name>` | O valor de cadeia que especifica a chave de um par chave-valor do OBJECT |

## Tipo de retorno

VARIANT

## Exemplos de SQL

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
