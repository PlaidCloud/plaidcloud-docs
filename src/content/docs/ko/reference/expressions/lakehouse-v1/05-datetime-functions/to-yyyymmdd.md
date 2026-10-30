---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD — 날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 UInt32 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 연도와 월 번호가 담긴 UInt32 숫자(YYYY * 10000 + MM * 100 + DD)로 변환합니다.

## Analyze 구문

```python
func.to_yyyymmdd(<expr>)
```

## Analyze 예제

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_YYYYMMDD(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|---------------|
| `<expr>`  | date/datetime |

## 반환 형식

`INT`, `YYYYMMDD` 형식으로 반환합니다.

## SQL 예제

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
