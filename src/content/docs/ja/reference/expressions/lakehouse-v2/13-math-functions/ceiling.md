---
title: CEILING (Lakehouse v2)
description: CEILING — 数値以上の最小の整数を返します。`CEIL` のエイリアスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

数値以上の最小の整数を返します。`CEIL` のエイリアスです。

## Analyzeの構文

```python
func.ceiling(<x>)
```

## Analyzeの例

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## SQLの構文

```sql
CEILING(<x>)
```

## SQLの例

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
