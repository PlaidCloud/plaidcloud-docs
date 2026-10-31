---
title: ROUND (Lakehouse v2)
description: ROUND — 数値を指定した小数桁数に丸めます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

数値を指定した小数桁数に丸めます。

## Analyzeの構文

```python
func.round(<x>[, <d>])
```

## Analyzeの例

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQLの構文

```sql
ROUND(<x>[, <d>])
```

## SQLの例

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
