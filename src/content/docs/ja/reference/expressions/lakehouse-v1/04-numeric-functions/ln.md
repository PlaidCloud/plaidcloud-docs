---
title: LN（Lakehouse v1）
description: LN — x の自然対数、つまり x の e を底とする対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

`x` の自然対数、つまり `x` の e を底とする対数を返します。x が 0.0E0 以下の場合、この関数は NULL を返します。

## Analyze 構文

```python
func.ln( <x> )
```

## Analyze の例

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL 構文

```sql
LN( <x> )
```

## SQL の例

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
