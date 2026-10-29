---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE：返回指定查询 ID 的查询配置文件。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

返回指定查询 ID 的查询配置文件，适用于性能分析和调试。

## Analyze 语法

```python
func.get_query_profile('query_id')
```

## Analyze 示例

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## SQL 语法

```sql
GET_QUERY_PROFILE(<query_id>)
```

## SQL 示例

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
