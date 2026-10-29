---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — 초기화에 사용하는 빈 백분위수 상태를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

초기화에 사용하는 빈 백분위수 상태를 반환합니다.

## Analyze 구문

```python
func.percentile_empty()
```

## Analyze 예제

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## SQL 구문

```sql
PERCENTILE_EMPTY()
```

## SQL 예제

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
