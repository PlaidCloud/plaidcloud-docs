---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL：返回详细的内存使用信息。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

返回详细的内存使用信息。

## Analyze 语法

```python
func.inspect_memory_detail()
```

## Analyze 示例

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## SQL 语法

```sql
INSPECT_MEMORY_DETAIL()
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
