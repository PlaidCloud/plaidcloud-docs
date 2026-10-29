---
title: FMOD (Lakehouse v2)
description: FMOD — 2つの数値を割ったときの浮動小数点の剰余を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

2つの数値を割ったときの浮動小数点の剰余を返します。

## Analyzeの構文

```python
func.fmod(<x>, <y>)
```

## Analyzeの例

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## SQLの構文

```sql
FMOD(<x>, <y>)
```

## SQLの例

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
