---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32 — 문자열의 xxHash32 32비트 해시 값을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

문자열의 xxHash32 32비트 해시 값을 계산합니다. 값은 UInt32로 반환되며, 인수가 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.xxhash32(<expr>)
```

## Analyze 예제

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## SQL 구문

```sql
XXHASH32(<expr>)
```

## SQL 예제

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
