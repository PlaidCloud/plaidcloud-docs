---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64 — 값을 FLOAT64 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

값을 FLOAT64 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_float64( <expr> )
```

## Analyze 예제

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 구문

```sql
TO_FLOAT64( <expr> )
```

## SQL 예제

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
