---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — Devuelve las vistas materializadas relacionadas con una tabla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

Devuelve las vistas materializadas relacionadas con una tabla.

## Sintaxis de Analyze

```python
func.inspect_related_mv(<db>, <table>)
```

## Ejemplos de Analyze

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
