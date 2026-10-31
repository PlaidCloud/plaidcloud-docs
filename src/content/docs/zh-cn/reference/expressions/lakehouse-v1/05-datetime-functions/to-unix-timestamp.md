---
title: TO_UNIX_TIMESTAMP（Lakehouse v1）
description: TO_UNIX_TIMESTAMP——将日期/时间格式的时间戳转换为 Unix 时间戳格式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

将日期/时间格式的时间戳转换为 Unix 时间戳格式。Unix 时间戳表示自 UTC 1970 年 1 月 1 日 00:00:00 以来经过的秒数。

## Analyze 语法

```python
func.to_unix_timestamp(<expr>)
```

## Analyze 示例

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## 参数

| 参数   | 说明         |
| ----------- | ------------------- |
| `<expr>`    | Timestamp           |

有关时间戳数据类型的详细信息，请参阅 Date & Time。

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
