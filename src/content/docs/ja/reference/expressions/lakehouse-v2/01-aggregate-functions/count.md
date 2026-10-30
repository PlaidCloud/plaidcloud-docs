---
title: COUNT（Lakehouse v2）
description: COUNT — 行数、またはNULLでない値の数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

行数、またはNULLでない値の数を返します。

## Analyzeの構文

```python
func.count()
```

## Analyzeの例

```python
func.count()
```

## SQLの構文

```sql
COUNT()
```

## SQLの例

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
