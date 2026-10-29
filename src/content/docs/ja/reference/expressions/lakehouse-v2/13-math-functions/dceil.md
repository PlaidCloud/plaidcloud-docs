---
title: DCEIL (Lakehouse v2)
description: DCEIL — `CEIL` のエイリアスです。[CEIL](../ceil/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

`CEIL` のエイリアスです。[CEIL](../ceil/) を参照してください。

## Analyzeの構文

```python
func.dceil(3.2)
```

## Analyzeの例

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## SQLの構文

```sql
DCEIL(<x>)
```

## SQLの例

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
