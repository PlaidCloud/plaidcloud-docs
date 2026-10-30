---
title: INSTR (Lakehouse v2)
description: INSTR：返回子字符串在字符串中首次出现的位置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

返回子字符串在字符串中首次出现的位置。

## Analyze 语法

```python
func.instr(<str>, <substr>)
```

## Analyze 示例

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL 语法

```sql
INSTR(<str>, <substr>)
```

## SQL 示例

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
