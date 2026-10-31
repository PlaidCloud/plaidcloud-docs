---
title: RPAD (Lakehouse v2)
description: RPAD：使用填充字符串在字符串右侧填充至指定长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

使用填充字符串在字符串右侧填充至指定长度。

## Analyze 语法

```python
func.rpad(<str>, <len>, <pad>)
```

## Analyze 示例

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## SQL 语法

```sql
RPAD(<str>, <len>, <pad>)
```

## SQL 示例

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
