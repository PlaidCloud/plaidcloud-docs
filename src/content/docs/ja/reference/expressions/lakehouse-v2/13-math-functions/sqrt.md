---
title: SQRT (Lakehouse v2)
description: SQRT — 数値の平方根を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

数値の平方根を返します。

## Analyzeの構文

```python
func.sqrt(<x>)
```

## Analyzeの例

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## SQLの構文

```sql
SQRT(<x>)
```

## SQLの例

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
