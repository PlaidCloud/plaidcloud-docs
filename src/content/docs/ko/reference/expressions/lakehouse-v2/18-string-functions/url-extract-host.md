---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — URL 문자열에서 호스트를 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

URL 문자열에서 호스트를 추출합니다.

## Analyze 구문

```python
func.url_extract_host(<url>)
```

## Analyze 예제

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## SQL 구문

```sql
URL_EXTRACT_HOST(<url>)
```

## SQL 예제

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```
