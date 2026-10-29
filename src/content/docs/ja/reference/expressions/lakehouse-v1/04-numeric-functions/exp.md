---
title: EXP（Lakehouse v1）
description: EXP — e（自然対数の底）の x 乗の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

e（自然対数の底）の `x` 乗の値を返します。

## Analyze 構文

```python
func.exp( <x> )
```

## Analyze の例

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## SQL 構文

```sql
EXP( <x> )
```

## SQL の例

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
