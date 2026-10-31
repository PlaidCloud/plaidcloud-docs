---
title: RADIANS (Lakehouse v2)
description: RADIANS — 度をラジアンに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

度をラジアンに変換します。

## Analyzeの構文

```python
func.radians(<x>)
```

## Analyzeの例

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## SQLの構文

```sql
RADIANS(<x>)
```

## SQLの例

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
