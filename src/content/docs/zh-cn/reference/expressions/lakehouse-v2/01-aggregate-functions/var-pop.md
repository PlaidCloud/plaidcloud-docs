---
title: VAR_POP (Lakehouse v2)
description: VAR_POP：返回总体方差，是 `VARIANCE_POP` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

返回总体方差，是 `VARIANCE_POP` 的别名。

## Analyze 语法

```python
func.var_pop(get_column(table, 'score'))
```

## Analyze 示例

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL 语法

```sql
VAR_POP(<score>)
```

## SQL 示例

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
