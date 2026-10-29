---
title: LENGTH (Lakehouse v1)
description: LENGTH — 指定した入力文字列またはバイナリ値の長さを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

指定した入力文字列またはバイナリ値の長さを返します。文字列の場合、長さは文字数を表し、UTF-8 の各文字は1文字として数えます。バイナリデータの場合、長さはバイト数に対応します。

## Analyze の構文

```python
func.length(<expr>)
```

## Analyze の例

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## SQL構文

```sql
LENGTH(<expr>)
```

## エイリアス

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## 戻り値の型

BIGINT

## SQLの例

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
