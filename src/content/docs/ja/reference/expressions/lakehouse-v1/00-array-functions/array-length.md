---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH — 配列の長さを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

配列の長さを返します。

## Analyzeの構文

```python
func.array_length( <array> )
```

## Analyzeの例

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_LENGTH( <array> )
```

## SQLの例

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
