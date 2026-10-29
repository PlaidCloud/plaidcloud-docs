---
title: DPOW (Lakehouse v2)
description: DPOW — `POW` のエイリアスです。[POW](../pow/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dpow.md
---

`POW` のエイリアスです。[POW](../pow/) を参照してください。

## Analyzeの構文

```python
func.dpow(2, 10)
```

## Analyzeの例

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQLの構文

```sql
DPOW(<x>)
```

## SQLの例

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
