---
title: IFNULL (Lakehouse v2)
description: IFNULL — 첫 번째 식이 NULL이 아니면 첫 번째 식을, NULL이면 두 번째 식을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

첫 번째 식이 NULL이 아니면 첫 번째 식을, NULL이면 두 번째 식을 반환합니다.

## Analyze 구문

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Analyze 예제

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## SQL 구문

```sql
IFNULL(<phone>, 'N/A')
```

## SQL 예제

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
