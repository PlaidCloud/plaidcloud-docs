---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS：检查位图是否包含特定值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

检查位图是否包含特定值。


## Analyze 语法

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Analyze 示例

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## SQL 示例

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
