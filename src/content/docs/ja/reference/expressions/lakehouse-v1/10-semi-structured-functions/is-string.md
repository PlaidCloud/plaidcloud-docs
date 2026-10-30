---
title: IS_STRING (Lakehouse v1)
description: IS_STRING — 入力のJSON値が文字列かどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-string.md
---

入力のJSON値が文字列かどうかをチェックします。

## Analyze構文

```python
func.is_string(<expr>)
```

## Analyzeの例

```python

func.is_string(func.parse_json('"abc"')), func.is_string(func.parse_json('123'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_string(func.parse_json('"abc"'))      │ func.is_string(func.parse_json('123'))           │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
IS_STRING( <expr> )
```

## 戻り値の型

入力のJSON値が文字列の場合は `true` を、それ以外の場合は `false` を返します。

## SQLの例

```sql
SELECT
  IS_STRING(PARSE_JSON('"abc"')),
  IS_STRING(PARSE_JSON('123'));

┌───────────────────────────────────────────────────────────────┐
│ is_string(parse_json('"abc"')) │ is_string(parse_json('123')) │
├────────────────────────────────┼──────────────────────────────┤
│ true                           │ false                        │
└───────────────────────────────────────────────────────────────┘
```
