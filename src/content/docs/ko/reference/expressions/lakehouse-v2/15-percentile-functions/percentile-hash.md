---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — 숫자 값에서 백분위수 상태를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

숫자 값에서 백분위수 상태를 계산합니다.

## Analyze 구문

```python
func.percentile_hash(<value>)
```

## Analyze 예제

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## SQL 구문

```sql
PERCENTILE_HASH(<value>)
```

## SQL 예제

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
