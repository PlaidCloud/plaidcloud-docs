---
title: COS（Lakehouse v1）
description: COS — x のコサインを返します。x はラジアンで指定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

`x` のコサインを返します。`x` はラジアンで指定します。

## Analyze 構文

```python
func.cos( <x> )
```

## Analyze の例

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## SQL 構文

```sql
COS( <x> )
```

## SQL の例

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
