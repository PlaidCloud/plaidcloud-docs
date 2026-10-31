---
title: DROUND (Lakehouse v2)
description: DROUND — `ROUND` のエイリアスです。[ROUND](../round/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

`ROUND` のエイリアスです。[ROUND](../round/) を参照してください。

## Analyzeの構文

```python
func.dround(3.14159, 2)
```

## Analyzeの例

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## SQLの構文

```sql
DROUND(<x>)
```

## SQLの例

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
