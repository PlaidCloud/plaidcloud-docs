---
title: TO_YEAR（Lakehouse v1）
description: TO_YEAR——将日期或带时间的日期（timestamp/datetime）转换为包含年份的 UInt16 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

将日期或带时间的日期（timestamp/datetime）转换为包含年份（公元）的 UInt16 数字。

## Analyze 语法

```python
func.to_year(<expr>)
```

## Analyze 示例

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_YEAR(<expr>)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 别名

- [YEAR](../year)

## 返回类型

 `SMALLINT`

## SQL 示例

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
