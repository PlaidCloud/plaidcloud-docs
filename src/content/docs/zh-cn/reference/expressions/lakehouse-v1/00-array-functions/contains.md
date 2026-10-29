---
title: CONTAINS (Lakehouse v1)
description: CONTAINS：检查数组是否包含特定元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

检查数组是否包含特定元素。


## Analyze 语法

```python
func.contains( <array>, <element> )
```

## Analyze 示例

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## SQL 语法

```sql
CONTAINS( <array>, <element> )
```

## 别名

- [ARRAY_CONTAINS](../array-contains)

## SQL 示例

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
