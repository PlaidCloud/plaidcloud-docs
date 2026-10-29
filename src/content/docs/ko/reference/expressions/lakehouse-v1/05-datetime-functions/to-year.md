---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR — 날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 연도 번호가 담긴 UInt16 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 연도 번호(서기)가 담긴 UInt16 숫자로 변환합니다.

## Analyze 구문

```python
func.to_year(<expr>)
```

## Analyze 예제

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_YEAR(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 별칭

- [YEAR](../year)

## 반환 형식

 `SMALLINT`

## SQL 예제

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
