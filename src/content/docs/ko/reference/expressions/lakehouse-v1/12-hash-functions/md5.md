---
title: MD5 (Lakehouse v1)
description: MD5 — 문자열의 MD5 128비트 체크섬을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

문자열의 MD5 128비트 체크섬을 계산합니다. 값은 16진수 32자리 문자열로 반환되며, 인수가 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.md5(<expr>)
```

## Analyze 예제

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## SQL 구문

```sql
MD5(<expr>)
```

## SQL 예제

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
