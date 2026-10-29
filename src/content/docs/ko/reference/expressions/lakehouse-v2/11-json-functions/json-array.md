---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — 값 목록에서 JSON 배열을 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

값 목록에서 JSON 배열을 만듭니다.

## Analyze 구문

```python
func.json_array(1, 'hello', None)
```

## Analyze 예제

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## SQL 구문

```sql
JSON_ARRAY(1, 'hello', None)
```

## SQL 예제

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
