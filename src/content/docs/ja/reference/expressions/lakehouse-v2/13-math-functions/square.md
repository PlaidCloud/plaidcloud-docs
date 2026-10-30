---
title: SQUARE (Lakehouse v2)
description: SQUARE — 数値の2乗を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

数値の2乗を返します。

## Analyzeの構文

```python
func.square(<x>)
```

## Analyzeの例

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## SQLの構文

```sql
SQUARE(<x>)
```

## SQLの例

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
