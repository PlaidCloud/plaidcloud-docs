---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — 정규식 패턴과 일치하는 모든 부분 문자열을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

정규식 패턴과 일치하는 모든 부분 문자열을 추출합니다.

## Analyze 구문

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Analyze 예제

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## SQL 구문

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## SQL 예제

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
