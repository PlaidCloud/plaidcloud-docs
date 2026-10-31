---
title: LN (Lakehouse v2)
description: LN — 数値の自然対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

数値の自然対数を返します。

## Analyzeの構文

```python
func.ln(<x>)
```

## Analyzeの例

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## SQLの構文

```sql
LN(<x>)
```

## SQLの例

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
