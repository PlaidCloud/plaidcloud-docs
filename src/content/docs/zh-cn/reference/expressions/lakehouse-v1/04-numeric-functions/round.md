---
title: ROUND（Lakehouse v1）
description: ROUND——将参数 x 四舍五入到 d 位小数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

将参数 x 四舍五入到 d 位小数。舍入算法取决于 x 的数据类型。未指定时，d 默认为 0。d 可以为负数，使值 x 小数点左侧的 d 位数字变为零。d 的最大绝对值为 30；超过 30（或 -30）的数位会被截断。

在计算中使用此函数的结果时，请注意其返回数据类型为 DOUBLE，可能带来精度问题并影响最终准确性：

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Analyze 语法

```python
func.round( <x, d> )
```

## Analyze 示例

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## SQL 语法

```sql
ROUND( <x, d> )
```

## SQL 示例

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
