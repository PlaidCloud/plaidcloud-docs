---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — 최상위 JSON 객체를 키-값 쌍 집합으로 확장합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

최상위 JSON 객체를 키-값 쌍 집합으로 확장합니다.

## Analyze 구문

```python
func.json_each(get_column(table, 'data'))
```

## Analyze 예제

```python
func.json_each(get_column(table, 'data'))
```

## SQL 구문

```sql
JSON_EACH(<data>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
