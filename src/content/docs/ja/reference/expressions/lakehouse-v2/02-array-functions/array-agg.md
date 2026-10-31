---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — 値を配列に集約します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

値を配列に集約します。

## Analyzeの構文

```python
func.array_agg(get_column(table, 'name'))
```

## Analyzeの例

```python
func.array_agg(get_column(table, 'name'))
```

## SQLの構文

```sql
ARRAY_AGG(<name>)
```

## SQLの例

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
