---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — 열 값의 직렬화된 형태의 크기를 바이트 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

열 값의 직렬화된 형태의 크기를 바이트 단위로 반환합니다.

## Analyze 구문

```python
func.column_size(get_column(table, 'name'))
```

## Analyze 예제

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## SQL 구문

```sql
COLUMN_SIZE(<expr>)
```

## SQL 예제

```sql
SELECT name, COLUMN_SIZE(name) FROM users LIMIT 3;

┌──────���┬───────────────────┐
│ name  │ column_size(name) │
├───────┼───────────────────┤
│ Alice │                 5 │
│ Bob   │                 3 │
│ Eve   │                 3 │
└───────┴───────────────────┘
```
