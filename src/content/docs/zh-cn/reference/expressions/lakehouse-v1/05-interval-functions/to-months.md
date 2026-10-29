---
title: TO_MONTHS（Lakehouse v1）
description: TO_MONTHS——将指定数量的个月转换为 Interval 类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-months.md
---

将指定数量的个月转换为 Interval 类型。

- 接受正整数、零和负整数作为输入。

## Analyze 语法

```python
func.to_months(<months>)
```

## Analyze 示例

```python
func.to_months(2)
┌──────────────────────────────────────────────────────┐
│ func.to_months(2)                                    │
├──────────────────────────────────────────────────────┤
│ 2 months                                             │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_MONTHS(<months>)
```

## 返回类型

Interval（以月表示）。

## SQL 示例

```sql
SELECT TO_MONTHS(2), TO_MONTHS(0), TO_MONTHS((- 2));

┌──────────────────────────────────────────────┐
│ to_months(2) │ to_months(0) │ to_months(- 2) │
├──────────────┼──────────────┼────────────────┤
│ 2 months     │ 00:00:00     │ -2 months      │
└──────────────────────────────────────────────┘
```
