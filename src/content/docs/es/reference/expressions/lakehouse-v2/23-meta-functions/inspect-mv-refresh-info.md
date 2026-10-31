---
title: INSPECT_MV_REFRESH_INFO (Lakehouse v2)
description: INSPECT_MV_REFRESH_INFO — Devuelve información de actualización de una vista materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

Devuelve información de actualización de una vista materializada.

## Sintaxis de Analyze

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Ejemplos de Analyze

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
