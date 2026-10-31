---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — 2つの数値の積を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

2つの数値の積を返します。

## Analyzeの構文

```python
func.multiply(<x>, <y>)
```

## Analyzeの例

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## SQLの構文

```sql
MULTIPLY(<x>, <y>)
```

## SQLの例

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
