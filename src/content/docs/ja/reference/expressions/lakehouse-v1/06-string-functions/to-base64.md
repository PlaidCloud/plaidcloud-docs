---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 — 文字列引数を Base64 エンコード形式に変換し、結果を文字列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

文字列引数を Base64 エンコード形式に変換し、結果を文字列として返します。
引数が文字列でない場合は、変換の前に文字列に変換されます。
引数が NULL の場合、結果は NULL になります。

## Analyze の構文

```python
func.to_base64(<v>)
```

## Analyze の例

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## SQL構文

```sql
TO_BASE64(<v>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<v>`     | 値。  |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
