---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID：返回当前会话中查询的最近一次查询 ID，索引可以是 (-1, 1, 1+2)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

返回当前会话中查询的最近一次查询 ID，索引可以是 (-1, 1, 1+2)……，超出范围的索引将返回空字符串。

## Analyze 语法

```python
func.last_query_id(<index>)
```

## Analyze 示例

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## SQL 语法

```sql
LAST_QUERY_ID(<index>)
```

## SQL 示例

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
