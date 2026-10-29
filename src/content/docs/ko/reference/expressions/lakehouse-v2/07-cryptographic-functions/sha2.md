---
title: SHA2 (Lakehouse v2)
description: SHA2 — 지정한 비트 길이(224, 256, 384 또는 512)로 문자열의 SHA-2 해시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

지정한 비트 길이(224, 256, 384 또는 512)로 문자열의 SHA-2 해시를 반환합니다.

## Analyze 구문

```python
func.sha2(<str>, <bit_length>)
```

## Analyze 예제

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## SQL 구문

```sql
SHA2(<str>, <bit_length>)
```

## SQL 예제

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
