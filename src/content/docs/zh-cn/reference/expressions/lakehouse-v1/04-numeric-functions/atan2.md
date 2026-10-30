---
title: ATAN2（Lakehouse v1）
description: ATAN2——返回两个变量 x 和 y 的反正切。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

返回两个变量 `x` 和 `y` 的反正切。它类似于计算 `y` / `x` 的反正切，不同之处在于会根据两个参数的符号来确定结果所在的象限。`ATAN(y, x)` 是 `ATAN2(y, x)` 的同义词。

## Analyze 语法

```python
func.atan2( <y, x> )
```

## Analyze 示例

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## SQL 语法

```sql
ATAN2( <y, x> )
```

## SQL 示例

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
