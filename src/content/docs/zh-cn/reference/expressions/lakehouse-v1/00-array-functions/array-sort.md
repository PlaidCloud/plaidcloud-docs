---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT：按升序对数组中的元素排序。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

按升序对数组中的元素排序。

## Analyze 语法

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| 参数    | 默认     | 说明                                                                                                                                    |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | 指定排序顺序为升序 (ASC) 或降序 (DESC)。                                                                    |
| nullposition | NULLS FIRST | 决定 NULL 值在排序结果中的位置：位于排序输出的开头 (NULLS FIRST) 或末尾 (NULLS LAST)。 |

## Analyze 示例

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| 参数    | 默认     | 说明                                                                                                                                    |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | 指定排序顺序为升序 (ASC) 或降序 (DESC)。                                                                    |
| nullposition | NULLS FIRST | 决定 NULL 值在排序结果中的位置：位于排序输出的开头 (NULLS FIRST) 或末尾 (NULLS LAST)。 |

## SQL 示例

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```
