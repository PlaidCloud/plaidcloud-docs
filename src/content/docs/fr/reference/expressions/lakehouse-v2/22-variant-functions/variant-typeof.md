---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — renvoie le nom du type d'une valeur VARIANT sous forme de chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

Renvoie le nom du type d'une valeur VARIANT sous forme de chaîne.

## Syntaxe Analyze

```python
func.variant_typeof(<variant>)
```

## Exemples Analyze

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## Syntaxe SQL

```sql
VARIANT_TYPEOF(<variant>)
```

## Exemples SQL

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
