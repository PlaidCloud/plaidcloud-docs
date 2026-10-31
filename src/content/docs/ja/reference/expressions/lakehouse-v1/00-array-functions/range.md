---
title: RANGE (Lakehouse v1)
description: RANGE — [start, end)の範囲の値を集めた配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

[start, end)の範囲の値を集めた配列を返します。

## Analyzeの構文

```python
func.range( <start>, <end> )
```

## Analyzeの例

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## SQLの構文

```sql
RANGE( <start>, <end> )
```

## SQLの例

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
