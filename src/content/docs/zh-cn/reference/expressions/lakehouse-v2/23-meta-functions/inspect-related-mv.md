---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV：返回与表相关的物化视图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

返回与表相关的物化视图。

## Analyze 语法

```python
func.inspect_related_mv(<db>, <table>)
```

## Analyze 示例

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## SQL 语法

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
