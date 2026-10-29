---
title: LOG2（Lakehouse v1）
description: LOG2 — x の 2 を底とする対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

`x` の 2 を底とする対数を返します。`x` が 0.0E0 以下の場合、この関数は NULL を返します。

## Analyze 構文

```python
func.log2( <x> )
```

## Analyze の例

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## SQL 構文

```sql
LOG2( <x> )
```

## SQL の例

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
