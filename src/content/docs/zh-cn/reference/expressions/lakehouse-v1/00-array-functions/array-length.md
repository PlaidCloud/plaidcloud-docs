---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH：返回数组的长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

返回数组的长度。

## Analyze 语法

```python
func.array_length( <array> )
```

## Analyze 示例

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_LENGTH( <array> )
```

## SQL 示例

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
