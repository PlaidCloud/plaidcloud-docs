---
title: FPOW (Lakehouse v2)
description: FPOW — `POW` のエイリアスです。[POW](../pow/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

`POW` のエイリアスです。[POW](../pow/) を参照してください。

## Analyzeの構文

```python
func.fpow(2, 10)
```

## Analyzeの例

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQLの構文

```sql
FPOW(<x>)
```

## SQLの例

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
