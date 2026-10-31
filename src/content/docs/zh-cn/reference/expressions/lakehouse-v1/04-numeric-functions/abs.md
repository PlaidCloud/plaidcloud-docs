---
title: ABS（Lakehouse v1）
description: ABS——返回 x 的绝对值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

返回 `x` 的绝对值。

## Analyze 语法

```python
func.abs( <x> )
```

## Analyze 示例

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## SQL 语法

```sql
ABS( <x> )
```

## SQL 示例

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
