---
title: "REVERSE (配列, Lakehouse v2)"
description: REVERSE — 要素を逆順にした配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

要素を逆順にした配列を返します。

## Analyzeの構文

```python
func.reverse([1, 2, 3])
```

## Analyzeの例

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## SQLの構文

```sql
REVERSE([1, 2, 3])
```

## SQLの例

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
