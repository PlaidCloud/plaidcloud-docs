---
title: LEAST (Lakehouse v1)
description: LEAST — 값 집합에서 최솟값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

값 집합에서 최솟값을 반환합니다.

## Analyze 구문

```python
func.least((<value1>, <value2> ...))
```

## Analyze 예시

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## SQL 구문

```sql
LEAST(<value1>, <value2> ...)
```

## SQL 예시

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
