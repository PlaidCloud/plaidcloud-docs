---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META：返回物化视图的元数据。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

返回物化视图的元数据。

## Analyze 语法

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Analyze 示例

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## SQL 语法

```sql
INSPECT_MV_META(<db>, <mv>)
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
