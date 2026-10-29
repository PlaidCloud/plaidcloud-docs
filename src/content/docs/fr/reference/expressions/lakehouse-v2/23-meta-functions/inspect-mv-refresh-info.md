---
title: INSPECT_MV_REFRESH_INFO (Lakehouse v2)
description: INSPECT_MV_REFRESH_INFO — renvoie les informations d'actualisation d'une vue matérialisée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

Renvoie les informations d'actualisation d'une vue matérialisée.

## Syntaxe Analyze

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Exemples Analyze

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## Syntaxe SQL

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
