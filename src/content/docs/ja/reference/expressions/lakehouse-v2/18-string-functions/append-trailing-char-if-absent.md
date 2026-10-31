---
title: APPEND_TRAILING_CHAR_IF_ABSENT（Lakehouse v2）
description: "PlaidCloud Lakehouse で APPEND_TRAILING_CHAR_IF_ABSENT 文字列関数を使用します。末尾に指定した文字がまだ付いていない場合に、その文字を文字列の末尾に追加します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

末尾に指定した文字がまだ付いていない場合に、その文字を文字列の末尾に追加します。

## Analyze 構文

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Analyze の例

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## SQL 構文

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## SQL の例

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
