---
title: TO_YYYYMM（Lakehouse v1）
description: TO_YYYYMM——将日期或带时间的日期（timestamp/datetime）转换为 UInt32 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

将日期或带时间的日期（timestamp/datetime）转换为包含年份和月份的 UInt32 数字。

## Analyze 语法

```python
func.to_yyyymm(<expr>)
```

## Analyze 示例

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_YYYYMM(<expr>)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 返回类型

`INT`，以 `YYYYMM` 格式返回。

## SQL 示例

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```
