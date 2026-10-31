---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — URL 문자열에서 지정한 부분을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

URL 문자열에서 지정한 부분을 추출합니다.

## Analyze 구문

```python
func.parse_url(<url>, <part>)
```

## Analyze 예제

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## SQL 구문

```sql
PARSE_URL(<url>, <part>)
```

## SQL 예제

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```
