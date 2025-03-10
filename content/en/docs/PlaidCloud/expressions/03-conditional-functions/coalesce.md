---
title: COALESCE
---

Returns the first non-NULL expression within its arguments; if all arguments are NULL, it returns NULL.

## Analyze Syntax
```python
func.coalesce(<expr1>[, <expr2> ...])
```

## Analyze Examples
```
func.coalesce(table.UOM,  'none', \n)

func.coalesce(get_column(table2, 'TECHNOLOGY_RATE'), 0.0)

func.coalesce(table_beta.adjusted_price, table_alpha.override_price, table_alpha.price) * table_beta.quantity_sold
```

## SQL Syntax

```sql
COALESCE(<expr1>[, <expr2> ...])
```

## SQL Examples

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