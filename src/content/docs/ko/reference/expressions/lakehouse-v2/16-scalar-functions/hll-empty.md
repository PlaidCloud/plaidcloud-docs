---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — 빈 HLL 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

빈 HLL 값을 반환합니다.

## Analyze 구문

```python
func.hll_empty()
```

## Analyze 예제

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## SQL 구문

```sql
HLL_EMPTY()
```

## SQL 예제

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
