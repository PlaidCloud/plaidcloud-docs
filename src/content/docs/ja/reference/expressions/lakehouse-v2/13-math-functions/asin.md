---
title: ASIN (Lakehouse v2)
description: ASIN — 数値の逆正弦をラジアンで返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

数値の逆正弦をラジアンで返します。

## Analyzeの構文

```python
func.asin(<x>)
```

## Analyzeの例

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## SQLの構文

```sql
ASIN(<x>)
```

## SQLの例

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
