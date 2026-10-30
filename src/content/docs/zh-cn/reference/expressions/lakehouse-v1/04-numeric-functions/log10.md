---
title: LOG10（Lakehouse v1）
description: LOG10——返回 x 以 10 为底的对数。参考。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

返回 `x` 以 10 为底的对数。如果 `x` 小于或等于 0.0E0，则函数返回 NULL。


## Analyze 语法

```python
func.log10( <x> )
```

## Analyze 示例

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## SQL 语法

```sql
LOG10( <x> )
```

## SQL 示例

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
