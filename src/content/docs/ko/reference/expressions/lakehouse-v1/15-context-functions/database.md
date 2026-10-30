---
title: DATABASE (Lakehouse v1)
description: DATABASE — 현재 선택된 데이터베이스의 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

현재 선택된 데이터베이스의 이름을 반환합니다. 선택된 데이터베이스가 없으면 이 함수는 `default`를 반환합니다.

## Analyze 구문

```python
func.database()
```

## Analyze 예제

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## SQL 구문

```sql
DATABASE()
```

## SQL 예제

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
