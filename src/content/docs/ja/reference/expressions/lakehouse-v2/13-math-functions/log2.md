---
title: LOG2 (Lakehouse v2)
description: LOG2 — 数値の底2の対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

数値の底2の対数を返します。

## Analyzeの構文

```python
func.log2(<x>)
```

## Analyzeの例

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## SQLの構文

```sql
LOG2(<x>)
```

## SQLの例

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
