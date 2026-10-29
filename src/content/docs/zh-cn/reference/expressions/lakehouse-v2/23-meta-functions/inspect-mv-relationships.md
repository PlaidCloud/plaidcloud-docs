---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS：返回物化视图的依赖关系。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

返回物化视图的依赖关系。

## Analyze 语法

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Analyze 示例

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## SQL 语法

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
