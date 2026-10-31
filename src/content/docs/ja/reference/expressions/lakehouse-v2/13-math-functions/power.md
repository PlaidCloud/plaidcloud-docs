---
title: POWER (Lakehouse v2)
description: POWER — ある数値を別の数値でべき乗した値を返します。`POW` のエイリアスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

ある数値を別の数値でべき乗した値を返します。`POW` のエイリアスです。

## Analyzeの構文

```python
func.power(<x>, <y>)
```

## Analyzeの例

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQLの構文

```sql
POWER(<x>, <y>)
```

## SQLの例

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
