---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — URL에서 사용할 수 있도록 문자열을 인코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

URL에서 사용할 수 있도록 문자열을 인코딩합니다.

## Analyze 구문

```python
func.url_encode(<str>)
```

## Analyze 예제

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## SQL 구문

```sql
URL_ENCODE(<str>)
```

## SQL 예제

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```
