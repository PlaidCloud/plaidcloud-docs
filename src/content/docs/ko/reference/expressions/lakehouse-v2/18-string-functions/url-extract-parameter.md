---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER — URL 문자열에서 쿼리 매개변수의 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

URL 문자열에서 쿼리 매개변수의 값을 추출합니다.

## Analyze 구문

```python
func.url_extract_parameter(<url>, <param>)
```

## Analyze 예제

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## SQL 구문

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## SQL 예제

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```
