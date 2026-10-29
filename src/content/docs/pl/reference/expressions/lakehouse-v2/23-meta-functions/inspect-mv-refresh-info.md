---
title: INSPECT_MV_REFRESH_INFO (Lakehouse v2)
description: INSPECT_MV_REFRESH_INFO — zwraca informacje o odświeżaniu widoku zmaterializowanego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

Zwraca informacje o odświeżaniu widoku zmaterializowanego.

## Składnia Analyze

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Przykłady Analyze

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## Składnia SQL

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
