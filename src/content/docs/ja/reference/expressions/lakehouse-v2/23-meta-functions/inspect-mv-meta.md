---
title: INSPECT_MV_META（Lakehouse v2）
description: INSPECT_MV_META — マテリアライズドビューのメタデータを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

マテリアライズドビューのメタデータを返します。

## Analyze 構文

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Analyze の例

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## SQL 構文

```sql
INSPECT_MV_META(<db>, <mv>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
