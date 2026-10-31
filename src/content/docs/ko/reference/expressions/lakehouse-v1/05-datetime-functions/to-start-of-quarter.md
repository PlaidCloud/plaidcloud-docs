---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER — 날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 분기의 첫날로 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 분기의 첫날로 내림합니다.
분기의 첫날은 1월 1일, 4월 1일, 7월 1일 또는 10월 1일 중 하나입니다.
날짜를 반환합니다.

## Analyze 구문

```python
func.to_start_of_quarter(<expr>)
```

## Analyze 예제

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_START_OF_QUARTER(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| `<expr>`   | date/timestamp |

## 반환 형식

`DATE`, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
