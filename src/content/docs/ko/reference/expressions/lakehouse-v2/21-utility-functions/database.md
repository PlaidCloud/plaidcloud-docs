---
title: DATABASE (Lakehouse v2)
description: DATABASE — 현재 데이터베이스의 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

현재 데이터베이스의 이름을 반환합니다.

## Analyze 구문

```python
func.database()
```

## Analyze 예제

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## SQL 구문

```sql
DATABASE()
```

## SQL 예제

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
