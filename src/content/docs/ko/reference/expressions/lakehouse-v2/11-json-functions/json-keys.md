---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — 최상위 JSON 객체의 키를 JSON 배열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

최상위 JSON 객체의 키를 JSON 배열로 반환합니다.

## Analyze 구문

```python
func.json_keys(get_column(table, 'data'))
```

## Analyze 예제

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## SQL 구문

```sql
JSON_KEYS(<data>)
```

## SQL 예제

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
