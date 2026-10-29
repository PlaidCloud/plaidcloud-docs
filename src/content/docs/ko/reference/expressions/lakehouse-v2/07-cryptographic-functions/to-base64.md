---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 — 문자열을 base64로 인코딩된 문자열로 인코딩합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

문자열을 base64로 인코딩된 문자열로 인코딩합니다.

## Analyze 구문

```python
func.to_base64(<str>)
```

## Analyze 예제

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## SQL 구문

```sql
TO_BASE64(<str>)
```

## SQL 예제

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
