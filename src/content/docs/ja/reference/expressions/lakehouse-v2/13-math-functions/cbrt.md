---
title: CBRT (Lakehouse v2)
description: CBRT — 数値の立方根を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

数値の立方根を返します。

## Analyzeの構文

```python
func.cbrt(<x>)
```

## Analyzeの例

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## SQLの構文

```sql
CBRT(<x>)
```

## SQLの例

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
