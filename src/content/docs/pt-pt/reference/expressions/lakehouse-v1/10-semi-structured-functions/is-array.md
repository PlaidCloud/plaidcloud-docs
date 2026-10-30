---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — Verifica se o valor de entrada é uma matriz JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

Verifica se o valor de entrada é uma matriz JSON. Tenha em atenção que uma matriz JSON não é o mesmo que o tipo de dados ARRAY. Uma matriz JSON é uma estrutura de dados habitualmente utilizada em JSON, que representa uma coleção ordenada de valores delimitada por parênteses retos `[ ]`. É um formato flexível para organizar e trocar vários tipos de dados, incluindo cadeias, números, booleanos, objetos e nulos. 

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

## Sintaxe do Analyze

```python
func.is_array(<expr>)
```

## Exemplos do Analyze

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IS_ARRAY( <expr> )
```

## Tipo de retorno

Devolve `true` se o valor de entrada for uma matriz JSON e `false` caso contrário.

## Exemplos de SQL

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
