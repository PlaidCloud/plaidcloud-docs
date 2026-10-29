---
title: INSPECT_MEMORY_DETAIL（Lakehouse v2）
description: INSPECT_MEMORY_DETAIL — メモリ使用量の詳細情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

メモリ使用量の詳細情報を返します。

## Analyze 構文

```python
func.inspect_memory_detail()
```

## Analyze の例

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## SQL 構文

```sql
INSPECT_MEMORY_DETAIL()
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
