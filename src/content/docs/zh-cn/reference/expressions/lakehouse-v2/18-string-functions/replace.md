---
title: REPLACE (Lakehouse v2)
description: REPLACE：将子字符串的所有匹配项替换为另一个子字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

将子字符串的所有匹配项替换为另一个子字符串。

## Analyze 语法

```python
func.replace(<str>, <old>, <new>)
```

## Analyze 示例

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## SQL 语法

```sql
REPLACE(<str>, <old>, <new>)
```

## SQL 示例

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
