---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID：返回最近执行的查询的 ID。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

返回最近执行的查询的 ID。

## Analyze 语法

```python
func.last_query_id()
```

## Analyze 示例

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## SQL 语法

```sql
LAST_QUERY_ID()
```

## SQL 示例

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
