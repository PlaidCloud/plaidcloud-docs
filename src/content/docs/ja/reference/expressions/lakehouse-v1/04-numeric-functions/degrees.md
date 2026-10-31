---
title: DEGREES (Lakehouse v1)
description: DEGREES — ラジアンで指定された引数 x を度に変換して返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

ラジアンで指定された引数 `x` を度に変換して返します。`x` はラジアンで指定します。

## Analyze 構文

```python
func.degrees( <x> )
```

## Analyze の例

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## SQL 構文

```sql
DEGREES( <x> )
```

## SQL の例

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
