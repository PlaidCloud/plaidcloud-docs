---
title: ATAN (Lakehouse v1)
description: ATAN — x의 아크탄젠트, 즉 탄젠트 값이 x인 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

`x`의 아크탄젠트, 즉 탄젠트 값이 `x`인 값을 반환합니다.

## Analyze 구문

```python
func.atan( <x> )
```

## Analyze 예시

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## SQL 구문

```sql
ATAN( <x> )
```

## SQL 예시

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
