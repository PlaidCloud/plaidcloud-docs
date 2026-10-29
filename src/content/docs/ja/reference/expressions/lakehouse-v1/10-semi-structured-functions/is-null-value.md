---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — 入力値がJSONのnullかどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

入力値がJSONの `null` かどうかをチェックします。ご注意：この関数が調べるのはJSONの `null` であり、SQLのNULLではありません。値がSQLのNULLかどうかをチェックするには、[IS_NULL](../../03-conditional-functions/is-null)を使用します。

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Analyze構文

```python
func.is_null_value(<expr>)
```

## Analyzeの例

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
IS_NULL_VALUE( <expr> )
```

## 戻り値の型

入力値がJSONの `null` の場合は `true` を、それ以外の場合は `false` を返します。

## SQLの例

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
