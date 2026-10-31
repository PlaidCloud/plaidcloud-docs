---
title: TOMORROW（Lakehouse v1）
description: TOMORROW——返回明天的日期，等同于 today() + 1。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

返回明天的日期，等同于 `today() + 1`。

## Analyze 语法

```python
func.tomorrow()
```

## Analyze 示例

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## SQL 语法

```sql
TOMORROW()
```

## 返回类型

`DATE`，返回“YYYY-MM-DD”格式的日期。

## SQL 示例

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
