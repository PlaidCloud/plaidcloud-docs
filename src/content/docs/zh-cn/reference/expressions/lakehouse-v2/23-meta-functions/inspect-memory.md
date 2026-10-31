---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY：返回当前节点的内存使用信息。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

返回当前节点的内存使用信息。

## Analyze 语法

```python
func.inspect_memory()
```

## Analyze 示例

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## SQL 语法

```sql
INSPECT_MEMORY()
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
