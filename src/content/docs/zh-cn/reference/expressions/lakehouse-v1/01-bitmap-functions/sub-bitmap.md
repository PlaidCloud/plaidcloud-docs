---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP：生成源位图的子位图，从起始索引开始，具有指定大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

生成源位图的子位图，从起始索引开始，具有指定大小。

## Analyze 语法

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Analyze 示例

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## SQL 示例

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
