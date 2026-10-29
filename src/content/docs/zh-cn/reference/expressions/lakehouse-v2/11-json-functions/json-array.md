---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — 根据一组值创建 JSON 数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

根据一组值创建 JSON 数组。

## Analyze 语法

```python
func.json_array(1, 'hello', None)
```

## Analyze 示例

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## SQL 语法

```sql
JSON_ARRAY(1, 'hello', None)
```

## SQL 示例

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
