---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — 값의 HLL 해시를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

값의 HLL 해시를 계산합니다.

## Analyze 구문

```python
func.hll_hash(<expr>)
```

## Analyze 예제

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## SQL 구문

```sql
HLL_HASH(<expr>)
```

## SQL 예제

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
