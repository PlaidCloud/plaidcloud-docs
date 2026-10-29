---
title: TIMESTAMP_DIFF（Lakehouse v1）
description: TIMESTAMP_DIFF——计算两个时间戳之间的差值，并以 INTERVAL 形式返回结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

计算两个时间戳之间的差值，并以 INTERVAL 形式返回结果。

## Analyze 语法

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Analyze 示例

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## 返回类型

INTERVAL（格式为 `hours:minutes:seconds`）。

## SQL 示例

此示例显示 2025 年 2 月 1 日与 2025 年 1 月 1 日之间的时间差为 744 小时，相当于 31 天：

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
