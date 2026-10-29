---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — 연결한 여러 문자열의 MD5 해시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

연결한 여러 문자열의 MD5 해시를 반환합니다.

## Analyze 구문

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Analyze 예제

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## SQL 구문

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## SQL 예제

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
