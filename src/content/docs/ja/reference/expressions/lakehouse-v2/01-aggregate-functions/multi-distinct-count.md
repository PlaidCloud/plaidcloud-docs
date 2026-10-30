---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT — 重複を除いた値の数を返します。COUNT(DISTINCT) と同等です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

重複を除いた値の数を返します。COUNT(DISTINCT) と同等です。

## Analyzeの構文

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Analyzeの例

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## SQLの構文

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## SQLの例

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
