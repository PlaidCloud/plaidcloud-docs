---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — URL 인코딩된 문자열을 디코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

URL 인코딩된 문자열을 디코딩합니다.

## Analyze 구문

```python
func.url_decode(<str>)
```

## Analyze 예제

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL 구문

```sql
URL_DECODE(<str>)
```

## SQL 예제

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```
