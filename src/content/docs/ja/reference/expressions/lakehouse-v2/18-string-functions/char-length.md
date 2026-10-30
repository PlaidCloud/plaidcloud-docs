---
title: CHAR_LENGTH（Lakehouse v2）
description: CHAR_LENGTH — 文字列の文字数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

文字列の文字数を返します。

## Analyze 構文

```python
func.char_length(<str>)
```

## Analyze の例

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## SQL 構文

```sql
CHAR_LENGTH(<str>)
```

## SQL の例

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
