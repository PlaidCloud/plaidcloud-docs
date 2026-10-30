---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — `LN` のエイリアスです。[LN](../ln/) を参照してください。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

`LN` のエイリアスです。[LN](../ln/) を参照してください。

## Analyzeの構文

```python
func.dlog1(2.718281828459045)
```

## Analyzeの例

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## SQLの構文

```sql
DLOG1(<x>)
```

## SQLの例

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
