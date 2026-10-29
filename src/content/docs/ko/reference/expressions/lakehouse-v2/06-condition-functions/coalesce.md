---
title: COALESCE (Lakehouse v2)
description: COALESCE — 식 목록에서 NULL이 아닌 첫 번째 식을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

식 목록에서 NULL이 아닌 첫 번째 식을 반환합니다.

## Analyze 구문

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Analyze 예제

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## SQL 구문

```sql
COALESCE(<nickname>, <name>)
```

## SQL 예제

```sql
SELECT COALESCE(nickname, first_name, 'Unknown') AS display_name FROM users;

┌──────────────┐
│ display_name │
├──────────────┤
│ Bob          │
│ Alice        │
│ Unknown      │
└──────────────┘
```
