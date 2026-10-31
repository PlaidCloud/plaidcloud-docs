---
title: CITY64WITHSEED（Lakehouse v1）
description: CITY64WITHSEED — 文字列のCity64WithSeed 64ビットハッシュを計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

文字列のCity64WithSeed 64ビットハッシュを計算します。

## Analyzeの構文

```python
func.city64withseed(<expr1>, <expr2>)
```

## Analyzeの例

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## SQLの構文

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## SQLの例

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```
