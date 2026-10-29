---
title: TO_JSON (Lakehouse v2)
description: TO_JSON — 将 SQL 值转换为 JSON 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/to-json.md
---

将 SQL 值转换为 JSON 值。

## Analyze 语法

```python
func.to_json(get_column(table, 'struct_col'))
```

## Analyze 示例

```python
func.to_json(func.named_struct('name', 'Alice', 'age', 30))

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL 语法

```sql
TO_JSON(<struct_col>)
```

## SQL 示例

```sql
SELECT TO_JSON(NAMED_STRUCT('name', 'Alice', 'age', 30));

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
