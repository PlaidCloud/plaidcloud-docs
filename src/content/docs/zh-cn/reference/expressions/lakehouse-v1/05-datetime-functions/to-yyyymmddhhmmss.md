---
title: TO_YYYYMMDDHHMMSS（Lakehouse v1）
description: TO_YYYYMMDDHHMMSS——将日期或带时间的日期（timestamp/datetime）转换为 UInt64 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

将日期或带时间的日期（timestamp/datetime）转换为包含年、月、日、时、分、秒的 UInt64 数字（YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss）。

## Analyze 语法

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Analyze 示例

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 返回类型

`BIGINT`，以 `YYYYMMDDhhmmss` 格式返回。

## SQL 示例

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```
