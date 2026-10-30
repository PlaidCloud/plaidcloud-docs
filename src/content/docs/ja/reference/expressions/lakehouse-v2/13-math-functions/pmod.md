---
title: PMOD (Lakehouse v2)
description: PMOD — 2つの数値を割ったときの正の剰余を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

2つの数値を割ったときの正の剰余を返します。

## Analyzeの構文

```python
func.pmod(<x>, <y>)
```

## Analyzeの例

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## SQLの構文

```sql
PMOD(<x>, <y>)
```

## SQLの例

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
