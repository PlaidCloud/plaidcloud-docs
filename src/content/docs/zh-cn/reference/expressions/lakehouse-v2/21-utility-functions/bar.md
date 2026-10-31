---
title: BAR (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 BAR 实用函数。返回范围内某个值的可视化条形字符串表示，适用于基于文本的可视化。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

返回范围内某个值的可视化条形字符串表示，适用于基于文本的可视化场景。

## Analyze 语法

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Analyze 示例

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## SQL 语法

```sql
BAR(<value>, <min>, <max>, <width>)
```

## SQL 示例

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
