---
title: LOG(x)（Lakehouse v1）
description: LOG(x)——返回 x 的自然对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

返回 `x` 的自然对数。如果 x 小于或等于 0.0E0，则函数返回 NULL。

## Analyze 语法

```python
 func.log( <x> )
```

## Analyze 示例

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL 语法

```sql
LOG( <x> )
```

## SQL 示例

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
