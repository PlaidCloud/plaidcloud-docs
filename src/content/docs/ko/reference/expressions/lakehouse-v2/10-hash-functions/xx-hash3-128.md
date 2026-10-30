---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — 값의 128비트 xxHash3 해시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

값의 128비트 xxHash3 해시를 반환합니다.

## Analyze 구문

```python
func.xx_hash3_128(<expr>[, ...])
```

## Analyze 예제

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 구문

```sql
XX_HASH3_128(<expr>[, ...])
```

## SQL 예제

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
