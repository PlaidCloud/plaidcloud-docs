---
title: NULLIF (Lakehouse v2)
description: NULLIF — 2 つの式が等しい場合は NULL を返し、等しくない場合は 1 つ目の式を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

2 つの式が等しい場合は NULL を返し、等しくない場合は 1 つ目の式を返します。

## Analyzeの構文

```python
func.nullif(get_column(table, 'value'), 0)
```

## Analyzeの例

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## SQLの構文

```sql
NULLIF(<value>, 0)
```

## SQLの例

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
