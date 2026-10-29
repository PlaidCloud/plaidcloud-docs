---
title: LIKE (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 LIKE 패턴 매칭 함수를 사용합니다. `%`(임의의 문자)와 `_`(문자 하나)를 사용하여 문자열을 패턴과 일치시킵니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

`%`(임의의 문자)와 `_`(문자 하나) 와일드카드를 사용하여 문자열을 패턴과 일치시킵니다.

## Analyze 구문

```python
func.like(<str> LIKE <pattern>)
```

## Analyze 예제

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL 구문

```sql
LIKE(<str> LIKE <pattern>)
```

## SQL 예제

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
