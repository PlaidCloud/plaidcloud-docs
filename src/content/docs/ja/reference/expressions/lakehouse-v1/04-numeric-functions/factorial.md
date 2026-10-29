---
title: FACTORIAL（Lakehouse v1）
description: FACTORIAL — x の階乗を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

`x` の階乗を返します。`x` が 0 以下の場合、この関数は 0 を返します。

## Analyze 構文

```python
func.factorial( <x> )
```

## Analyze の例

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## SQL 構文

```sql
FACTORIAL( <x> )
```

## SQL の例

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
