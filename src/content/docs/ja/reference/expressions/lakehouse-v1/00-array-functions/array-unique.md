---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE — 配列内の一意の要素（NULLを除く）の数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

配列内の一意の要素（NULLを除く）の数を返します。

## Analyzeの構文

```python
func.array_unique( <array> )
```

## Analyzeの例

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_UNIQUE( <array> )
```

## SQLの例

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
