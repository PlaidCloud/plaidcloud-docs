---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64 — 문자열의 xxHash64 64비트 해시 값을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

문자열의 xxHash64 64비트 해시 값을 계산합니다. 값은 UInt64로 반환되며, 인수가 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.xxhash64(<expr>)
```

## Analyze 예제

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## SQL 구문

```sql
XXHASH64(<expr>)
```

## SQL 예제

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
