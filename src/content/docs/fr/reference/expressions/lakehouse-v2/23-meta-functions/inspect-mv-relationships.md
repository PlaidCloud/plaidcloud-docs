---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — renvoie les relations de dépendance d'une vue matérialisée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

Renvoie les relations de dépendance d'une vue matérialisée.

## Syntaxe Analyze

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Exemples Analyze

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## Syntaxe SQL

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
