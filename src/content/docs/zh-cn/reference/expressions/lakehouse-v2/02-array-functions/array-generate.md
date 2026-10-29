---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE：生成由连续值组成的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

生成由连续值组成的数组。

## Analyze 语法

```python
func.array_generate(1, 5)
```

## Analyze 示例

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## SQL 语法

```sql
ARRAY_GENERATE(1, 5)
```

## SQL 示例

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
