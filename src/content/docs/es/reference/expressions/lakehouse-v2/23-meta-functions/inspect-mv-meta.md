---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META — Devuelve metadatos de una vista materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

Devuelve metadatos de una vista materializada.

## Sintaxis de Analyze

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Ejemplos de Analyze

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_MV_META(<db>, <mv>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
