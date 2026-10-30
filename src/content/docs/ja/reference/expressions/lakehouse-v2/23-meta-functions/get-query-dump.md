---
title: GET_QUERY_DUMP（Lakehouse v2）
description: GET_QUERY_DUMP — 診断用のクエリダンプを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

診断用のクエリダンプを返します。

## Analyze 構文

```python
func.get_query_dump(<query>)
```

## Analyze の例

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## SQL 構文

```sql
GET_QUERY_DUMP(<query>)
```

## SQL の例

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
