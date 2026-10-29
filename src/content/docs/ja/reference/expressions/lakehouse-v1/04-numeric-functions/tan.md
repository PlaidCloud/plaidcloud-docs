---
title: TAN（Lakehouse v1）
description: TAN — x のタンジェントを返します。x はラジアンで指定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

`x` のタンジェントを返します。`x` はラジアンで指定します。

## Analyze 構文

```python
func.tan( <x> )
```

## Analyze の例

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## SQL 構文

```sql
TAN( <x> )
```

## SQL の例

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
