---
title: REGEXP_COUNT (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 REGEXP_COUNT 패턴 매칭 함수를 사용합니다. 정규식 패턴이 문자열에 나타나는 횟수를 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

정규식 패턴이 문자열에 나타나는 횟수를 반환합니다.

## Analyze 구문

```python
func.regexp_count(<str>, <pattern>)
```

## Analyze 예제

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## SQL 구문

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## SQL 예제

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
