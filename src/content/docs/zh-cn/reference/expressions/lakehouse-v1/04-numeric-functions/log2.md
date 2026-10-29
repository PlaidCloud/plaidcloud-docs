---
title: LOG2（Lakehouse v1）
description: LOG2——返回 x 以 2 为底的对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

返回 `x` 以 2 为底的对数。如果 `x` 小于或等于 0.0E0，则函数返回 NULL。

## Analyze 语法

```python
func.log2( <x> )
```

## Analyze 示例

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## SQL 语法

```sql
LOG2( <x> )
```

## SQL 示例

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
