---
title: REGEXP (Lakehouse v2)
description: REGEXP — 문자열이 정규식 패턴과 일치하는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

문자열이 정규식 패턴과 일치하는지 확인합니다.

## Analyze 구문

```python
func.regexp(<str> REGEXP <pattern>)
```

## Analyze 예제

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## SQL 구문

```sql
REGEXP(<str> REGEXP <pattern>)
```

## SQL 예제

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```
