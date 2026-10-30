---
title: LAST_DAY（Lakehouse v1）
description: LAST_DAY——返回指定区间（周、月、季度或年）的最后一天。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

根据提供的日期或时间戳，返回指定区间（周、月、季度或年）的最后一天。

## Analyze 语法

```python
func.last_day(<date_expression>, <interval>)
```

## Analyze 示例

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
LAST_DAY(<date_expression>, <interval>)
```

| 参数                | 说明                                                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 用于计算指定区间最后一天的 DATE 或 TIMESTAMP 值。                                                             |
| `<interval>`        | 要查找最后一天的区间类型。可接受的值为 `week`、`month`、`quarter` 和 `year`。                                 |

## 返回类型

日期。

## SQL 示例

假设需要根据交易的任意日期（例如 2024-11-13）确定账单日期，账单日期始终为当月最后一天：

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
