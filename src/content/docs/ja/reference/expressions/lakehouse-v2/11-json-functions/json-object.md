---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — キーと値のペアからJSONオブジェクトを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

キーと値のペアからJSONオブジェクトを作成します。

## Analyzeの構文

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Analyzeの例

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQLの構文

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## SQLの例

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
