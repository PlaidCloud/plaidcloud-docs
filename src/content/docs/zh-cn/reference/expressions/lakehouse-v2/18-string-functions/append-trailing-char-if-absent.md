---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 APPEND_TRAILING_CHAR_IF_ABSENT 字符串函数。如果字符串末尾尚无指定字符，则追加该字符。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

如果字符串末尾尚无指定字符，则追加该字符。

## Analyze 语法

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Analyze 示例

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## SQL 语法

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## SQL 示例

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
