---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — `FLOOR` のエイリアスです。[FLOOR](../floor/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

`FLOOR` のエイリアスです。[FLOOR](../floor/) を参照してください。

## Analyzeの構文

```python
func.dfloor(3.7)
```

## Analyzeの例

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## SQLの構文

```sql
DFLOOR(<x>)
```

## SQLの例

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
