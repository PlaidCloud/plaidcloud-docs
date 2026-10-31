---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — 入力値がJSON配列かどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

入力値がJSON配列かどうかをチェックします。ご注意：JSON配列は、ARRAYデータ型とは異なります。JSON配列はJSONでよく使われるデータ構造で、角かっこ `[ ]` で囲まれた値の順序付きコレクションを表します。文字列、数値、ブール値、オブジェクト、nullなど、さまざまなデータ型を含めることができ、データの整理や交換に柔軟に使える形式です。

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

## Analyze構文

```python
func.is_array(<expr>)
```

## Analyzeの例

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
IS_ARRAY( <expr> )
```

## 戻り値の型

入力値がJSON配列の場合は `true` を、それ以外の場合は `false` を返します。

## SQLの例

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
