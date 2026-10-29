---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — JSON 문서의 지정한 경로에서 요소를 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

JSON 문서의 지정한 경로에서 요소를 제거합니다.

## Analyze 구문

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Analyze 예제

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## SQL 구문

```sql
JSON_REMOVE(<data>, '$.temp')
```

## SQL 예제

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
