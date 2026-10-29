---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — Devuelve las relaciones de dependencia de una vista materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

Devuelve las relaciones de dependencia de una vista materializada.

## Sintaxis de Analyze

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Ejemplos de Analyze

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
