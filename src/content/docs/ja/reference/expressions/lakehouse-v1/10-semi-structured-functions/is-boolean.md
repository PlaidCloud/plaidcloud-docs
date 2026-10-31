---
title: IS_BOOLEAN (Lakehouse v1)
description: IS_BOOLEAN — 入力のJSON値がブール値かどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-boolean.md
---

入力のJSON値がブール値かどうかをチェックします。

## Analyze構文

```python
func.is_boolean(<expr>)
```

## Analyzeの例

```python

func.is_boolean(func.parse_json('true')), func.is_boolean(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_boolean(func.parse_json('true')) │ func.is_boolean(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
IS_BOOLEAN( <expr> )
```

## 戻り値の型

入力のJSON値がブール値の場合は `true` を、それ以外の場合は `false` を返します。

## SQLの例

```sql
SELECT
  IS_BOOLEAN(PARSE_JSON('true')),
  IS_BOOLEAN(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────────┐
│ is_boolean(parse_json('true')) │ is_boolean(parse_json('[1,2,3]')) │
├────────────────────────────────┼───────────────────────────────────┤
│ true                           │ false                             │
└────────────────────────────────────────────────────────────────────┘
```
