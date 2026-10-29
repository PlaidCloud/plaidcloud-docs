---
title: "LOG(b, x)（Lakehouse v1）"
description: LOG(b, x) — x の b を底とする対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

`x` の b を底とする対数を返します。`x` が 0.0E0 以下の場合、この関数は NULL を返します。

## Analyze 構文

```python
func.log( <b, x> )
```

## Analyze の例

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## SQL 構文

```sql
LOG( <b, x> )
```

## SQL の例

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
