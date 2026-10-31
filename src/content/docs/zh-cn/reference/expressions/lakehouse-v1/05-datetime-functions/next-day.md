---
title: NEXT_DAY（Lakehouse v1）
description: NEXT_DAY——返回给定日期或时间戳之后下一个指定星期几的日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

返回给定日期或时间戳之后下一个指定星期几的日期。

## Analyze 语法

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze 示例

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| 参数                | 说明                                                                                                                                                                     |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 用于计算指定星期几下一次出现日期的 `DATE` 或 `TIMESTAMP` 值。                                                                                                            |
| `<target_day>`      | 要查找下一次出现日期的目标星期几。可接受的值包括 `monday`、`tuesday`、`wednesday`、`thursday`、`friday`、`saturday` 和 `sunday`。                                       |

## 返回类型

日期。

## SQL 示例

要查找特定日期（例如 2024-11-13）之后的下一个星期一：

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
