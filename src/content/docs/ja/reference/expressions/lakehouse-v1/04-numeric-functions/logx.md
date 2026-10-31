---
title: LOG(x)（Lakehouse v1）
description: LOG(x) — x の自然対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

`x` の自然対数を返します。x が 0.0E0 以下の場合、この関数は NULL を返します。

## Analyze 構文

```python
 func.log( <x> )
```

## Analyze の例

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL 構文

```sql
LOG( <x> )
```

## SQL の例

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
