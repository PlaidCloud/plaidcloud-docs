---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND — 配列に要素を追加します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

配列に要素を追加します。

## Analyzeの構文

```python
func.array_append( <array>, <element>)
```

## Analyzeの例

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_APPEND( <array>, <element>)
```

## SQLの例

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
