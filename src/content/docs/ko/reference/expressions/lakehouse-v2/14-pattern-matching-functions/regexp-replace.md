---
title: REGEXP_REPLACE (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 REGEXP_REPLACE 패턴 매칭 함수를 사용합니다. 정규식 패턴과 일치하는 부분 문자열을 대체 문자열로 바꿉니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

정규식 패턴과 일치하는 부분 문자열을 대체 문자열로 바꿉니다.

## Analyze 구문

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Analyze 예제

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL 구문

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## SQL 예제

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
