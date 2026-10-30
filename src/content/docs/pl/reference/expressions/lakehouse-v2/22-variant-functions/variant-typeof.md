---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — zwraca nazwę typu wartości VARIANT jako ciąg.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

Zwraca nazwę typu wartości VARIANT jako ciąg.

## Składnia Analyze

```python
func.variant_typeof(<variant>)
```

## Przykłady Analyze

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## Składnia SQL

```sql
VARIANT_TYPEOF(<variant>)
```

## Przykłady SQL

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
