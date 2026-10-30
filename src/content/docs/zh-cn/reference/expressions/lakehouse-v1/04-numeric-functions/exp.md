---
title: EXP（Lakehouse v1）
description: EXP——返回 e（自然对数的底）的 x 次幂。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

返回 e（自然对数的底）的 `x` 次幂。

## Analyze 语法

```python
func.exp( <x> )
```

## Analyze 示例

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## SQL 语法

```sql
EXP( <x> )
```

## SQL 示例

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
