---
title: PREVIOUS_DAY（Lakehouse v1）
description: PREVIOUS_DAY——返回给定日期之前最近一个指定星期几的日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

返回给定日期或时间戳之前最近一个指定星期几的日期。

## Analyze 语法

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze 示例

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| 参数                | 说明                                                                                                                                                                     |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 用于计算指定星期几上一次出现日期的 `DATE` 或 `TIMESTAMP` 值。                                                                                                            |
| `<target_day>`      | 要查找上一次出现日期的目标星期几。可接受的值包括 `monday`、`tuesday`、`wednesday`、`thursday`、`friday`、`saturday` 和 `sunday`。                                       |

## 返回类型

日期。

## SQL 示例

如果需要查找给定日期（例如 2024-11-13）之前的上一个星期五：

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
