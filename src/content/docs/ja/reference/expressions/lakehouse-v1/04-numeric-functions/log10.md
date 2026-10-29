---
title: LOG10（Lakehouse v1）
description: LOG10 — x の 10 を底とする対数を返します。リファレンスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

`x` の 10 を底とする対数を返します。`x` が 0.0E0 以下の場合、この関数は NULL を返します。


## Analyze 構文

```python
func.log10( <x> )
```

## Analyze の例

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## SQL 構文

```sql
LOG10( <x> )
```

## SQL の例

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
