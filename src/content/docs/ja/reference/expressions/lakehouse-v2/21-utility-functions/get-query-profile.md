---
title: GET_QUERY_PROFILE（Lakehouse v2）
description: GET_QUERY_PROFILE — 指定したクエリ ID のクエリプロファイルを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

指定したクエリ ID のクエリプロファイルを返します。パフォーマンス分析やデバッグに便利です。

## Analyze 構文

```python
func.get_query_profile('query_id')
```

## Analyze の例

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## SQL 構文

```sql
GET_QUERY_PROFILE(<query_id>)
```

## SQL の例

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
