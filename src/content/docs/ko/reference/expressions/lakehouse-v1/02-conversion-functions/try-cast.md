---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST — 값을 한 데이터 형식에서 다른 데이터 형식으로 변환합니다. 오류가 발생하면 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

값을 한 데이터 형식에서 다른 데이터 형식으로 변환합니다. 오류가 발생하면 NULL을 반환합니다.

참고: [CAST](../cast)

## Analyze 구문

```python
func.try_cast( <expr>, <data_type> )
```

## Analyze 예제

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## SQL 구문

```sql
TRY_CAST( <expr> AS <data_type> )
```

## SQL 예제

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
