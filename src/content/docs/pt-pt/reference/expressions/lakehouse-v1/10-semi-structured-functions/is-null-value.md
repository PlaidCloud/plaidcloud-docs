---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — verifica se o valor de entrada é um null JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

Verifica se o valor de entrada é um `null` JSON. Tenha em atenção que esta função examina o `null` JSON, não o NULL de SQL. Para verificar se um valor é NULL de SQL, utilize [IS_NULL](../../03-conditional-functions/is-null).

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Sintaxe do Analyze

```python
func.is_null_value(<expr>)
```

## Exemplos do Analyze

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IS_NULL_VALUE( <expr> )
```

## Tipo de retorno

Devolve `true` se o valor de entrada for um `null` JSON e `false` caso contrário.

## Exemplos de SQL

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
