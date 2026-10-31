---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — extrai o valor de um VARIANT que contém um OBJECT através do field_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

Extrai o valor de um `VARIANT` que contém um `OBJECT` através do field_name.
O valor é devolvido como `Variant` ou `NULL` se qualquer um dos argumentos for `NULL`.

`GET_IGNORE_CASE` é semelhante a `GET`, mas aplica correspondência sem distinção entre maiúsculas e minúsculas aos nomes dos campos.
Primeiro procura o nome de campo exatamente igual; se não o encontrar, procura por ordem alfabética o nome de campo sem distinção entre maiúsculas e minúsculas.

## Sintaxe do Analyze

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Exemplos do Analyze

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## Argumentos

| Argumentos     | Descrição                                                              |
|----------------|------------------------------------------------------------------------|
| `<variant>`    | O valor VARIANT que contém um ARRAY ou um OBJECT                       |
| `<field_name>` | O valor de cadeia que especifica a chave de um par chave-valor do OBJECT |

## Tipo de retorno

VARIANT

## Exemplos de SQL

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
