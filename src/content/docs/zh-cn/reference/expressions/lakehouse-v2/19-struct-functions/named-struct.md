---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT：使用指定的字段名和值创建结构体。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

使用指定的字段名和值创建结构体。

## Analyze 语法

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Analyze 示例

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## SQL 语法

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## SQL 示例

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
