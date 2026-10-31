---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META — renvoie les métadonnées d'une vue matérialisée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

Renvoie les métadonnées d'une vue matérialisée.

## Syntaxe Analyze

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Exemples Analyze

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## Syntaxe SQL

```sql
INSPECT_MV_META(<db>, <mv>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
