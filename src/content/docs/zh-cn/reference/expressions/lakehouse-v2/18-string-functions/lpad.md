---
title: LPAD (Lakehouse v2)
description: LPAD：使用填充字符串在字符串左侧填充至指定长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

使用填充字符串在字符串左侧填充至指定长度。

## Analyze 语法

```python
func.lpad(<str>, <len>, <pad>)
```

## Analyze 示例

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## SQL 语法

```sql
LPAD(<str>, <len>, <pad>)
```

## SQL 示例

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
