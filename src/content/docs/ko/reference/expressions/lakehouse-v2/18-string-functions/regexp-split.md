---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT — 정규식 패턴으로 문자열을 분할하여 부분 문자열 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

정규식 패턴으로 문자열을 분할하여 부분 문자열 배열을 반환합니다.

## Analyze 구문

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Analyze 예제

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## SQL 구문

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## SQL 예제

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
