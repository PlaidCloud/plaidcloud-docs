---
title: INSPECT_MV_REFRESH_INFO (Lakehouse v2)
description: INSPECT_MV_REFRESH_INFO — devolve informação de atualização de uma vista materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

Devolve informação de atualização de uma vista materializada.

## Sintaxe do Analyze

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Exemplos do Analyze

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## Sintaxe SQL

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## Exemplos SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
