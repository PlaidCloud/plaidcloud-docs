---
title: PLUS（Lakehouse v1）
description: PLUS — 2 つの数値または小数値の合計を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

2 つの数値または小数値の合計を計算します。

## Analyze 構文

```python
func.plus(<number1>, <number2>)
```

## Analyze の例

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## SQL 構文

```sql
PLUS(<number1>, <number2>)
```

## エイリアス

- [ADD](../add)

## SQL の例

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```
