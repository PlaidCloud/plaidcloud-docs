---
title: COALESCE (Lakehouse v1)
description: COALESCE：返回其参数中第一个非 NULL 的表达式；如果所有参数均为 NULL，则返回 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/coalesce.md
---

返回其参数中第一个非 NULL 的表达式；如果所有参数均为 NULL，则返回 NULL。

## Analyze 语法
```python
func.coalesce(<expr1>[, <expr2> ...])
```

## Analyze 示例

```sql
func.coalesce(table.UOM,  'none', \n)

func.coalesce(get_column(table2, 'TECHNOLOGY_RATE'), 0.0)

func.coalesce(table_beta.adjusted_price, table_alpha.override_price, table_alpha.price) * table_beta.quantity_sold
```

## SQL 语法

```sql
COALESCE(<expr1>[, <expr2> ...])
```

## SQL 示例

```sql
SELECT COALESCE(1), COALESCE(1, NULL), COALESCE(NULL, 1, 2);

┌────────────────────────────────────────────────────────┐
│ coalesce(1) │ coalesce(1, null) │ coalesce(null, 1, 2) │
├─────────────┼───────────────────┼──────────────────────┤
│           1 │                 1 │                    1 │
└────────────────────────────────────────────────────────┘

SELECT COALESCE('a'), COALESCE('a', NULL), COALESCE(NULL, 'a', 'b');

┌────────────────────────────────────────────────────────────────┐
│ coalesce('a') │ coalesce('a', null) │ coalesce(null, 'a', 'b') │
├───────────────┼─────────────────────┼──────────────────────────┤
│ a             │ a                   │ a                        │
└────────────────────────────────────────────────────────────────┘
```
