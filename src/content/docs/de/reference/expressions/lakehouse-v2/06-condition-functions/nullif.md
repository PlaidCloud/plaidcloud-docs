---
title: NULLIF (Lakehouse v2)
description: NULLIF – gibt NULL zurück, wenn zwei Ausdrücke gleich sind, andernfalls den ersten Ausdruck.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

Gibt NULL zurück, wenn zwei Ausdrücke gleich sind, andernfalls den ersten Ausdruck.

## Analyze-Syntax

```python
func.nullif(get_column(table, 'value'), 0)
```

## Analyze-Beispiele

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## SQL-Syntax

```sql
NULLIF(<value>, 0)
```

## SQL-Beispiele

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
