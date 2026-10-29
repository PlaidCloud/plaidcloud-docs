---
title: SIN（Lakehouse v1）
description: SIN — x のサインを返します。x はラジアンで指定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

`x` のサインを返します。`x` はラジアンで指定します。

## Analyze 構文

```python
func.sin( <x> )
```

## Analyze の例

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## SQL 構文

```sql
SIN( <x> )
```

## SQL の例

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
