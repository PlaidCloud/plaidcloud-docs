---
title: ABS (Lakehouse v2)
description: ABS — 数値の絶対値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

数値の絶対値を返します。

## Analyzeの構文

```python
func.abs(<x>)
```

## Analyzeの例

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## SQLの構文

```sql
ABS(<x>)
```

## SQLの例

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
