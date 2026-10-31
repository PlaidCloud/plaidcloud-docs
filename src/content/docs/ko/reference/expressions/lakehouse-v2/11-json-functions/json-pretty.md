---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — 가독성을 위해 JSON 값에 들여쓰기를 적용하여 서식을 지정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

가독성을 위해 JSON 값에 들여쓰기를 적용하여 서식을 지정합니다.

## Analyze 구문

```python
func.json_pretty(get_column(table, 'data'))
```

## Analyze 예제

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## SQL 구문

```sql
JSON_PRETTY(<data>)
```

## SQL 예제

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
