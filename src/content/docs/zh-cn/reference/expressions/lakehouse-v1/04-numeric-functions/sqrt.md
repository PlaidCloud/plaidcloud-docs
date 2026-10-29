---
title: SQRT（Lakehouse v1）
description: SQRT——返回非负数 x 的平方根。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

返回非负数 `x` 的平方根。输入为负数时返回 Nan。

## Analyze 语法

```python
func.sqrt( <x> )
```

## Analyze 示例

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## SQL 语法

```sql
SQRT( <x> )
```

## SQL 示例

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
