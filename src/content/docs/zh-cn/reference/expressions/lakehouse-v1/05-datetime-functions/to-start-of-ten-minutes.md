---
title: TO_START_OF_TEN_MINUTES（Lakehouse v1）
description: TO_START_OF_TEN_MINUTES——将带时间的日期（timestamp/datetime）向下取整到十分钟间隔的起点。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-ten-minutes.md
---

将带时间的日期（timestamp/datetime）向下取整到十分钟间隔的起点。

## Analyze 语法

```python
func.to_start_of_ten_minutes(<expr>)
```

## Analyze 示例

```python
func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')     │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_START_OF_TEN_MINUTES(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<expr>`  | timestamp   |

## 返回类型

`TIMESTAMP`，返回“YYYY-MM-DD hh:mm:ss.ffffff”格式的日期。

## SQL 示例

```sql
SELECT
  to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────────┐
│ to_start_of_ten_minutes('2023-11-12 09:38:18.165575') │
│                       Timestamp                       │
├───────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                   │
└───────────────────────────────────────────────────────┘
```
