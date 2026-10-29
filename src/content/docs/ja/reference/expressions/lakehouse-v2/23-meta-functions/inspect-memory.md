---
title: INSPECT_MEMORY（Lakehouse v2）
description: INSPECT_MEMORY — 現在のノードのメモリ使用量の情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

現在のノードのメモリ使用量の情報を返します。

## Analyze 構文

```python
func.inspect_memory()
```

## Analyze の例

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## SQL 構文

```sql
INSPECT_MEMORY()
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
