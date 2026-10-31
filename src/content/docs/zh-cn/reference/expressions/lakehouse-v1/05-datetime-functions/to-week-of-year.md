---
title: TO_WEEK_OF_YEAR（Lakehouse v1）
description: TO_WEEK_OF_YEAR——计算给定日期在一年中的周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

计算给定日期在一年中的周数。

ISO 周编号规则如下：1 月 4 日始终属于第一周。如果 1 月 1 日是星期四，则从 12 月 29 日（星期一）到 1 月 4 日（星期日）的这一周为 ISO 第 1 周。如果 1 月 1 日是星期五，则从 1 月 4 日（星期一）到 1 月 10 日（星期日）的这一周为 ISO 第 1 周。

## Analyze 语法

```python
func.to_week_of_year(<expr>)
```

## Analyze 示例

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 别名

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## 返回类型

返回表示一年中周数的整数，范围为 1 到 53。

## SQL 示例

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
