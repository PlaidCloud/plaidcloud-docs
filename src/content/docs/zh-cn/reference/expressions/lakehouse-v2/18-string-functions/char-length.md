---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH：返回字符串中的字符数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

返回字符串中的字符数。

## Analyze 语法

```python
func.char_length(<str>)
```

## Analyze 示例

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## SQL 语法

```sql
CHAR_LENGTH(<str>)
```

## SQL 示例

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
