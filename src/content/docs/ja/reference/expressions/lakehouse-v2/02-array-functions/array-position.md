---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — 要素が最初に現れる位置を返します（1 始まり）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

要素が最初に現れる位置を返します（1 始まり）。

## Analyzeの構文

```python
func.array_position([10, 20, 30], 20)
```

## Analyzeの例

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## SQLの構文

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## SQLの例

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
