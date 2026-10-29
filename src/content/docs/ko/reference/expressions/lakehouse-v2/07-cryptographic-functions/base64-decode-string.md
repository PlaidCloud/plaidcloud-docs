---
title: BASE64_DECODE_STRING (Lakehouse v2)
description: BASE64_DECODE_STRING — base64로 인코딩된 문자열을 VARCHAR 문자열로 디코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-string.md
---

base64로 인코딩된 문자열을 VARCHAR 문자열로 디코딩합니다.

## Analyze 구문

```python
func.base64_decode_string(<str>)
```

## Analyze 예제

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 구문

```sql
BASE64_DECODE_STRING(<str>)
```

## SQL 예제

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
