---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — 부호를 사용해 사분면을 결정하여 y/x의 아크탄젠트를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

부호를 사용해 사분면을 결정하여 y/x의 아크탄젠트를 반환합니다.

## Analyze 구문

```python
func.atan2(<y>, <x>)
```

## Analyze 예제

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL 구문

```sql
ATAN2(<y>, <x>)
```

## SQL 예제

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
