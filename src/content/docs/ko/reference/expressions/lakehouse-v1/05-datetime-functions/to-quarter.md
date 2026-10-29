---
title: TO_QUARTER (Lakehouse v1)
description: TO_QUARTER — 지정한 날짜 또는 타임스탬프에서 분기(1, 2, 3 또는 4)를 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

지정한 날짜 또는 타임스탬프에서 분기(1, 2, 3 또는 4)를 가져옵니다.

## Analyze 구문

```python
func.to_quarter(<expr>)
```

## Analyze 예시

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_QUARTER( <date_or_time_expr> )
```

## 별칭

- [QUARTER](../quarter)

## 반환 형식

정수입니다.

## SQL 예시

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
