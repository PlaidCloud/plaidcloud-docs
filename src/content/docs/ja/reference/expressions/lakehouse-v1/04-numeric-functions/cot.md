---
title: COT（Lakehouse v1）
description: COT — x のコタンジェントを返します。x はラジアンで指定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

`x` のコタンジェントを返します。`x` はラジアンで指定します。

## Analyze 構文

```python
func.cot( <x> )
```

## Analyze の例

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## SQL 構文

```sql
COT( <x> )
```

## SQL の例

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
