---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — JSON 문서의 지정한 경로에 값을 설정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

JSON 문서의 지정한 경로에 값을 설정합니다.

## Analyze 구문

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Analyze 예제

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## SQL 구문

```sql
JSON_SET(<data>, '$.age', 31)
```

## SQL 예제

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
