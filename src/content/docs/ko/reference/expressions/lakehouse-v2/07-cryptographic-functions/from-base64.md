---
title: FROM_BASE64 (Lakehouse v2)
description: FROM_BASE64 — base64로 인코딩된 문자열을 디코딩합니다. `BASE64_DECODE_STRING`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/from-base64.md
---

base64로 인코딩된 문자열을 디코딩합니다. `BASE64_DECODE_STRING`의 별칭입니다.

## Analyze 구문

```python
func.from_base64(<str>)
```

## Analyze 예제

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 구문

```sql
FROM_BASE64(<str>)
```

## SQL 예제

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
