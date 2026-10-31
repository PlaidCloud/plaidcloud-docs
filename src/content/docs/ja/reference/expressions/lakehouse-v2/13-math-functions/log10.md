---
title: LOG10 (Lakehouse v2)
description: LOG10 — 数値の常用対数（底10）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

数値の常用対数（底10）を返します。

## Analyzeの構文

```python
func.log10(<x>)
```

## Analyzeの例

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## SQLの構文

```sql
LOG10(<x>)
```

## SQLの例

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
