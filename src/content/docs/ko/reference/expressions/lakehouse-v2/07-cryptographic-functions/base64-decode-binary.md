---
title: BASE64_DECODE_BINARY (Lakehouse v2)
description: BASE64_DECODE_BINARY — base64로 인코딩된 문자열을 바이너리 값으로 디코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/base64-decode-binary.md
---

base64로 인코딩된 문자열을 바이너리 값으로 디코딩합니다.

## Analyze 구문

```python
func.base64_decode_binary(<str>)
```

## Analyze 예제

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL 구문

```sql
BASE64_DECODE_BINARY(<str>)
```

## SQL 예제

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
