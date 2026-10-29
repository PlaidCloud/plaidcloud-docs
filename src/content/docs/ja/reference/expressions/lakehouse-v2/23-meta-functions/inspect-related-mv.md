---
title: INSPECT_RELATED_MV（Lakehouse v2）
description: INSPECT_RELATED_MV — テーブルに関連するマテリアライズドビューを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

テーブルに関連するマテリアライズドビューを返します。

## Analyze 構文

```python
func.inspect_related_mv(<db>, <table>)
```

## Analyze の例

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## SQL 構文

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
