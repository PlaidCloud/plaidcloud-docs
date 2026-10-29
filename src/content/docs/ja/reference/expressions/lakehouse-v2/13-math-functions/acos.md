---
title: ACOS (Lakehouse v2)
description: ACOS — 数値の逆余弦をラジアンで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

数値の逆余弦をラジアンで返します。

## Analyzeの構文

```python
func.acos(<x>)
```

## Analyzeの例

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## SQLの構文

```sql
ACOS(<x>)
```

## SQLの例

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
