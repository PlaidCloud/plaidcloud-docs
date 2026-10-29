---
title: TO_YYYYMMDDHH（Lakehouse v1）
description: TO_YYYYMMDDHH——将给定的日期或时间戳格式化为“YYYYMMDDHH”格式的字符串表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

将给定的日期或时间戳格式化为“YYYYMMDDHH”（年、月、日、时）格式的字符串表示。

## Analyze 语法

```python
func.to_yyyymmddhh(<expr>)
```

## Analyze 示例

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_YYYYMMDDHH(<expr>)
```

## 参数

| 参数 | 说明   |
|-----------|---------------|
| `<expr>`  | date/datetime |

## 返回类型

返回“YYYYMMDDHH”格式的无符号 64 位整数（UInt64）。

## SQL 示例

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
