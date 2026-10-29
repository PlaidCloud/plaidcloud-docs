---
title: INSPECT_MV_RELATIONSHIPS（Lakehouse v2）
description: INSPECT_MV_RELATIONSHIPS — マテリアライズドビューの依存関係を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

マテリアライズドビューの依存関係を返します。

## Analyze 構文

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Analyze の例

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## SQL 構文

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
