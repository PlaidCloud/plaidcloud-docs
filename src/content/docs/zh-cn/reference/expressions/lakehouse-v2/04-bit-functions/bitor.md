---
title: BITOR (Lakehouse v2)
description: BITOR：返回两个数值的按位或结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

返回两个数值的按位或结果。

## Analyze 语法

```python
func.bitor(<x>, <y>)
```

## Analyze 示例

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## SQL 语法

```sql
BITOR(<x>, <y>)
```

## SQL 示例

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
