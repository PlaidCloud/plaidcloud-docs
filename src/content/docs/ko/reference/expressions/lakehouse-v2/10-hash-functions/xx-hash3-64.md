---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — 값의 64비트 xxHash3 해시를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

값의 64비트 xxHash3 해시를 반환합니다.

## Analyze 구문

```python
func.xx_hash3_64(<expr>[, ...])
```

## Analyze 예제

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## SQL 구문

```sql
XX_HASH3_64(<expr>[, ...])
```

## SQL 예제

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
