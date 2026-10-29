---
title: COSH (Lakehouse v2)
description: COSH — 数値の双曲線余弦を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

数値の双曲線余弦を返します。

## Analyzeの構文

```python
func.cosh(<x>)
```

## Analyzeの例

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQLの構文

```sql
COSH(<x>)
```

## SQLの例

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
