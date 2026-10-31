---
title: LOG2 (Lakehouse v2)
description: LOG2 — 返回数值以 2 为底的对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

返回数值以 2 为底的对数。

## Analyze 语法

```python
func.log2(<x>)
```

## Analyze 示例

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL 语法

```sql
LOG2(<x>)
```

## SQL 示例

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
