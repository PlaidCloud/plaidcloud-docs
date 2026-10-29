---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — JSON 객체 또는 배열의 요소 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

JSON 객체 또는 배열의 요소 수를 반환합니다.

## Analyze 구문

```python
func.json_length(get_column(table, 'data'))
```

## Analyze 예제

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## SQL 구문

```sql
JSON_LENGTH(<data>)
```

## SQL 예제

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
