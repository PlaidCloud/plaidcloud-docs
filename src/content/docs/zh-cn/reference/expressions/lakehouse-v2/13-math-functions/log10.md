---
title: LOG10 (Lakehouse v2)
description: LOG10 — 返回数值以 10 为底的对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

返回数值以 10 为底的对数。

## Analyze 语法

```python
func.log10(<x>)
```

## Analyze 示例

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL 语法

```sql
LOG10(<x>)
```

## SQL 示例

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
