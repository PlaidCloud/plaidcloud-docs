---
title: FLOOR (Lakehouse v2)
description: FLOOR — 数値以下の最大の整数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

数値以下の最大の整数を返します。

## Analyzeの構文

```python
func.floor(<x>)
```

## Analyzeの例

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## SQLの構文

```sql
FLOOR(<x>)
```

## SQLの例

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
