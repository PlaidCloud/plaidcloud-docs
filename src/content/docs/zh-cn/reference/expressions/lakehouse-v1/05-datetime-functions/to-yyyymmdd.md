---
title: TO_YYYYMMDD（Lakehouse v1）
description: TO_YYYYMMDD——将日期或带时间的日期（timestamp/datetime）转换为 UInt32 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

将日期或带时间的日期（timestamp/datetime）转换为包含年、月、日的 UInt32 数字（YYYY * 10000 + MM * 100 + DD）。

## Analyze 语法

```python
func.to_yyyymmdd(<expr>)
```

## Analyze 示例

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_YYYYMMDD(<expr>)
```

## 参数

| 参数 | 说明   |
|-----------|---------------|
| `<expr>`  | date/datetime |

## 返回类型

`INT`，以 `YYYYMMDD` 格式返回。

## SQL 示例

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
