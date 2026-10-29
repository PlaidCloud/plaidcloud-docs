---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — 키-값 쌍에서 JSON 객체를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

키-값 쌍에서 JSON 객체를 만듭니다.

## Analyze 구문

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Analyze 예제

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL 구문

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## SQL 예제

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
