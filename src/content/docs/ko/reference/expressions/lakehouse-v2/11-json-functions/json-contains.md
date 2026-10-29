---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — JSON 문서의 지정한 경로에 특정 값이 포함되어 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

JSON 문서의 지정한 경로에 특정 값이 포함되어 있는지 확인합니다.

## Analyze 구문

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Analyze 예제

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## SQL 예제

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
