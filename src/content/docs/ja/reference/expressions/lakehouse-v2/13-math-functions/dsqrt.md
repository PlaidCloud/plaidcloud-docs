---
title: DSQRT (Lakehouse v2)
description: DSQRT — `SQRT` のエイリアスです。[SQRT](../sqrt/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

`SQRT` のエイリアスです。[SQRT](../sqrt/) を参照してください。

## Analyzeの構文

```python
func.dsqrt(144)
```

## Analyzeの例

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## SQLの構文

```sql
DSQRT(<x>)
```

## SQLの例

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
