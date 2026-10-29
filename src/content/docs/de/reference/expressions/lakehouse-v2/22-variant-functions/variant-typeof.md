---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — Gibt den Typnamen eines VARIANT-Werts als Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

Gibt den Typnamen eines VARIANT-Werts als Zeichenfolge zurück.

## Analyze-Syntax

```python
func.variant_typeof(<variant>)
```

## Analyze-Beispiele

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## SQL-Syntax

```sql
VARIANT_TYPEOF(<variant>)
```

## SQL-Beispiele

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
