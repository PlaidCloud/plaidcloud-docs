---
title: COUNT_IF（Lakehouse v2）
description: COUNT_IF — 式がTRUEになる行数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

式がTRUEになる行数を返します。

## Analyzeの構文

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Analyzeの例

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## SQLの構文

```sql
COUNT_IF(<salary> > 80000)
```

## SQLの例

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
