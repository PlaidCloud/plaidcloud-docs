---
title: EXP (Lakehouse v2)
description: EXP — eを数値でべき乗した値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

eを数値でべき乗した値を返します。

## Analyzeの構文

```python
func.exp(<x>)
```

## Analyzeの例

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## SQLの構文

```sql
EXP(<x>)
```

## SQLの例

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
