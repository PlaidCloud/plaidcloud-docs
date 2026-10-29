---
title: VARIANT_QUERY (Lakehouse v2)
description: "Verwenden Sie die Variant-Funktion VARIANT_QUERY in PlaidCloud Lakehouse. Fragt mit einem Pfadausdruck einen Wert aus einem VARIANT-Objekt ab und gibt einen VARIANT zurück."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

Fragt mit einem Pfadausdruck einen Wert aus einem VARIANT-Objekt ab und gibt einen VARIANT zurück.

## Analyze-Syntax

```python
func.variant_query(<variant>, <path>)
```

## Analyze-Beispiele

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## SQL-Syntax

```sql
VARIANT_QUERY(<variant>, <path>)
```

## SQL-Beispiele

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
