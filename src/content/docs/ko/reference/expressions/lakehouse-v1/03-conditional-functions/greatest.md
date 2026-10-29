---
title: GREATEST (Lakehouse v1)
description: GREATEST — 값 집합에서 최댓값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

값 집합에서 최댓값을 반환합니다.

## Analyze 구문

```python
func.greatest(<value1>, <value2> ...)
```

## Analyze 예시

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## SQL 구문

```sql
GREATEST(<value1>, <value2> ...)
```

## SQL 예시

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
