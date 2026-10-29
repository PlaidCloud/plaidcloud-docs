---
title: INSPECT_MV_REFRESH_INFO (Lakehouse v2)
description: INSPECT_MV_REFRESH_INFO — gibt Aktualisierungsinformationen zu einer materialisierten Ansicht zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

Gibt Aktualisierungsinformationen zu einer materialisierten Ansicht zurück.

## Analyze-Syntax

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Analyze-Beispiele

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## SQL-Syntax

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
