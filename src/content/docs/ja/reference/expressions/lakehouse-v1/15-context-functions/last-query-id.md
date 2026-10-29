---
title: LAST_QUERY_ID（Lakehouse v1）
description: LAST_QUERY_ID — 現在のセッションにおける直近のクエリのクエリIDを返します。インデックスには(-1、1、1+2)などを指定できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

現在のセッションにおける直近のクエリのクエリIDを返します。インデックスには(-1、1、1+2)...などを指定できます。範囲外のインデックスを指定すると、空の文字列が返されます。

## Analyzeの構文

```python
func.last_query_id(<index>)
```

## Analyzeの例

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## SQLの構文

```sql
LAST_QUERY_ID(<index>)
```

## SQLの例

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
