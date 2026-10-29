---
title: TO_START_OF_WEEK（Lakehouse v1）
description: TO_START_OF_WEEK——返回日期或带时间的日期所在周的第一天。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

返回日期或带时间的日期（timestamp/datetime）所在周的第一天。
一周的第一天可以是星期日或星期一，由参数 `mode` 指定。

## Analyze 语法

```python
func.to_start_of_week(<expr>)
```

## Analyze 示例

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## 参数

| 参数 | 说明                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------|
| `<expr>`  | date/timestamp                                                                                      |
| `[mode]`  | 可选。为 0 时结果为星期日，否则结果为星期一。默认值为 0 |

## 返回类型

`DATE`，返回“YYYY-MM-DD”格式的日期。

## SQL 示例

```sql
SELECT
  to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_week('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-11-12                                     │
└────────────────────────────────────────────────┘
```
