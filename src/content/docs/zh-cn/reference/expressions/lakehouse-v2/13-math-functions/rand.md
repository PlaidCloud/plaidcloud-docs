---
title: RAND (Lakehouse v2)
description: RAND — 返回介于 0（含）和 1（不含）之间的随机浮点值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

返回介于 0（含）和 1（不含）之间的随机浮点值。

## Analyze 语法

```python
func.rand([<seed>])
```

## Analyze 示例

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## SQL 语法

```sql
RAND([<seed>])
```

## SQL 示例

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
