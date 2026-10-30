---
title: ROW (Lakehouse v2)
description: ROW：根据值列表创建结构体。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

根据值列表创建结构体。

## Analyze 语法

```python
func.row(<val1>[, <val2>, ...])
```

## Analyze 示例

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## SQL 语法

```sql
ROW(<val1>[, <val2>, ...])
```

## SQL 示例

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
