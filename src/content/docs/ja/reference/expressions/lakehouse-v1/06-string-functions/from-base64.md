---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 — Base64 エンコード規則でエンコードされた文字列を受け取り、デコード結果をバイナリとして返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

Base64 エンコード規則でエンコードされた文字列を受け取り、デコード結果をバイナリとして返します。
引数が NULL の場合、または有効な Base64 文字列でない場合、結果は NULL になります。

## Analyze の構文

```python
func.from_base64(<expr>)
```

## Analyze の例

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## SQL構文

```sql
FROM_BASE64(<expr>)
```

## 引数

| 引数 | 説明       |
|-----------|-------------------|
| `<expr>`  | 文字列値。 |

## 戻り値の型

`BINARY`

## SQLの例

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
