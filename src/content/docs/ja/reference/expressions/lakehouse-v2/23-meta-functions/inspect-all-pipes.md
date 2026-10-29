---
title: INSPECT_ALL_PIPES（Lakehouse v2）
description: INSPECT_ALL_PIPES — すべてのパイプオブジェクトに関する情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

すべてのパイプオブジェクトに関する情報を返します。

## Analyze 構文

```python
func.inspect_all_pipes()
```

## Analyze の例

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## SQL 構文

```sql
INSPECT_ALL_PIPES()
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
