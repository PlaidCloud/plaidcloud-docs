---
title: INITCAP (Lakehouse v2)
description: INITCAP：将字符串中每个单词的首字母大写。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

将字符串中每个单词的首字母大写。

## Analyze 语法

```python
func.initcap(<str>)
```

## Analyze 示例

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## SQL 语法

```sql
INITCAP(<str>)
```

## SQL 示例

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
