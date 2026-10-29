---
title: TO_START_OF_HOUR（Lakehouse v1）
description: TO_START_OF_HOUR——将带时间的日期（timestamp/datetime）向下取整到整点开始时刻。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-hour.md
---

将带时间的日期（timestamp/datetime）向下取整到整点开始时刻。

## Analyze 语法

```python
func.to_start_of_hour(<expr>)
```

## Analyze 示例

```python
func.to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_hour('2023-11-12 09:38:18.165575')            │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_START_OF_HOUR(<expr>)
```

## 参数

| 参数      | 说明        |
|-----------|-------------|
| `<expr>`  | 时间戳      |

## 返回类型

`TIMESTAMP`，以“YYYY-MM-DD hh:mm:ss.ffffff”格式返回日期。

## SQL 示例

```sql
SELECT
  to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_hour('2023-11-12 09:38:18.165575') │
│                    Timestamp                   │
├────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                            │
└────────────────────────────────────────────────┘
```
