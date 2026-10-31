---
title: CEIL (Lakehouse v2)
description: CEIL — 数値以上の最小の整数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

数値以上の最小の整数を返します。

## Analyzeの構文

```python
func.ceil(<x>)
```

## Analyzeの例

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## SQLの構文

```sql
CEIL(<x>)
```

## SQLの例

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
