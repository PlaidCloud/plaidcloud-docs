---
title: "GET（数组，Lakehouse v1）"
description: GET：按索引（从 1 开始）返回数组中的元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

按索引（从 1 开始）返回数组中的元素。

## Analyze 语法

```python
func.get( <array>, <index> )
```

## Analyze 示例

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## SQL 语法

```sql
GET( <array>, <index> )
```

## 别名

- [ARRAY_GET](../array-get)

## SQL 示例

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
