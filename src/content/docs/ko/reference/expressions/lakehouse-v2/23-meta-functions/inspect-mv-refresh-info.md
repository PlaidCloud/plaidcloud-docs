---
title: INSPECT_MV_REFRESH_INFO (Lakehouse v2)
description: INSPECT_MV_REFRESH_INFO — 구체화된 뷰의 새로 고침 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

구체화된 뷰의 새로 고침 정보를 반환합니다.

## Analyze 구문

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Analyze 예제

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## SQL 구문

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
