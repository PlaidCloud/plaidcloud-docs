---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — `LOG10` のエイリアスです。[LOG10](../log10/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

`LOG10` のエイリアスです。[LOG10](../log10/) を参照してください。

## Analyzeの構文

```python
func.dlog10(1000)
```

## Analyzeの例

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## SQLの構文

```sql
DLOG10(<x>)
```

## SQLの例

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
