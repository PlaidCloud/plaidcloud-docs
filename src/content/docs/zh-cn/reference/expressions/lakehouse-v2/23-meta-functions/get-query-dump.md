---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP：返回用于诊断的查询转储。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

返回用于诊断的查询转储。

## Analyze 语法

```python
func.get_query_dump(<query>)
```

## Analyze 示例

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## SQL 语法

```sql
GET_QUERY_DUMP(<query>)
```

## SQL 示例

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
