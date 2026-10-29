---
title: INSPECT_MV_REFRESH_INFO（Lakehouse v2）
description: INSPECT_MV_REFRESH_INFO — マテリアライズドビューの更新情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-refresh-info.md
---

マテリアライズドビューの更新情報を返します。

## Analyze 構文

```python
func.inspect_mv_refresh_info(<db>, <mv>)
```

## Analyze の例

```python
func.inspect_mv_refresh_info('mydb', 'my_mv')

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```

## SQL 構文

```sql
INSPECT_MV_REFRESH_INFO(<db>, <mv>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_MV_REFRESH_INFO('mydb', 'my_mv'));

┌────────────────┐
│ (refresh info)  │
└────────────────┘
```
