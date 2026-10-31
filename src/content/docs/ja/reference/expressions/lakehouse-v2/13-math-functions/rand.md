---
title: RAND (Lakehouse v2)
description: RAND — 0以上1未満のランダムな浮動小数点値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

0以上1未満のランダムな浮動小数点値を返します。

## Analyzeの構文

```python
func.rand([<seed>])
```

## Analyzeの例

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## SQLの構文

```sql
RAND([<seed>])
```

## SQLの例

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
