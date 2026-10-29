---
title: MOD (Lakehouse v2)
description: MOD — 2つの数値を割ったときの剰余を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

2つの数値を割ったときの剰余を返します。

## Analyzeの構文

```python
func.mod(<x>, <y>)
```

## Analyzeの例

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## SQLの構文

```sql
MOD(<x>, <y>)
```

## SQLの例

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
