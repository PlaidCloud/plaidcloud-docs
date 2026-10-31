---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — 값의 32비트 MurmurHash3 해시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

값의 32비트 MurmurHash3 해시를 반환합니다.

## Analyze 구문

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Analyze 예제

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## SQL 구문

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## SQL 예제

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
