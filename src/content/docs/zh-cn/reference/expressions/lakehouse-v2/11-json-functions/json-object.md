---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — 根据键值对创建 JSON 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

根据键值对创建 JSON 对象。

## Analyze 语法

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Analyze 示例

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL 语法

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## SQL 示例

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
