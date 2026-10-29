---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC — 여러 문자열의 MD5 해시를 128비트 숫자 값으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

여러 문자열의 MD5 해시를 128비트 숫자 값으로 반환합니다.

## Analyze 구문

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Analyze 예제

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 구문

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## SQL 예제

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
