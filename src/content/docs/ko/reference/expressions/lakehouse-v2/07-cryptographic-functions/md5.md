---
title: MD5 (Lakehouse v2)
description: MD5 — 문자열의 MD5 해시를 32자리 16진수 문자열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

문자열의 MD5 해시를 32자리 16진수 문자열로 반환합니다.

## Analyze 구문

```python
func.md5(<str>)
```

## Analyze 예제

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## SQL 구문

```sql
MD5(<str>)
```

## SQL 예제

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
