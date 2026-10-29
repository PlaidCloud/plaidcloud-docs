---
title: ATAN2（Lakehouse v1）
description: ATAN2 — 2 つの変数 x と y のアークタンジェントを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

2 つの変数 `x` と `y` のアークタンジェントを返します。`y` / `x` のアークタンジェントを計算する場合と似ていますが、両方の引数の符号を使って結果の象限を決定する点が異なります。`ATAN(y, x)` は `ATAN2(y, x)` の同義語です。

## Analyze 構文

```python
func.atan2( <y, x> )
```

## Analyze の例

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## SQL 構文

```sql
ATAN2( <y, x> )
```

## SQL の例

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
