---
title: DEXP (Lakehouse v2)
description: DEXP — `EXP` のエイリアスです。[EXP](../exp/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

`EXP` のエイリアスです。[EXP](../exp/) を参照してください。

## Analyzeの構文

```python
func.dexp(1)
```

## Analyzeの例

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## SQLの構文

```sql
DEXP(<x>)
```

## SQLの例

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
