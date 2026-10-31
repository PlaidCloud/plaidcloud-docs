---
title: LAST_QUERY_ID（Lakehouse v2）
description: LAST_QUERY_ID — 直近に実行されたクエリの ID を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

直近に実行されたクエリの ID を返します。

## Analyze 構文

```python
func.last_query_id()
```

## Analyze の例

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## SQL 構文

```sql
LAST_QUERY_ID()
```

## SQL の例

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
