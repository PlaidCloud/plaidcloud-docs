---
title: RANDOM (Lakehouse v2)
description: RANDOM — 0から1の間のランダムな浮動小数点値を返します。`RAND` のエイリアスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

0から1の間のランダムな浮動小数点値を返します。`RAND` のエイリアスです。

## Analyzeの構文

```python
func.random([<seed>])
```

## Analyzeの例

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## SQLの構文

```sql
RANDOM([<seed>])
```

## SQLの例

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
