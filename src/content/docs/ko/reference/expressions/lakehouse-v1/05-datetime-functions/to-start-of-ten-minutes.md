---
title: TO_START_OF_TEN_MINUTES (Lakehouse v1)
description: TO_START_OF_TEN_MINUTES — 시간이 포함된 날짜(timestamp/datetime)를 10분 간격의 시작 시점으로 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-ten-minutes.md
---

시간이 포함된 날짜(timestamp/datetime)를 10분 간격의 시작 시점으로 내림합니다.

## Analyze 구문

```python
func.to_start_of_ten_minutes(<expr>)
```

## Analyze 예제

```python
func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')     │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_START_OF_TEN_MINUTES(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr>`  | timestamp   |

## 반환 형식

`TIMESTAMP`, “YYYY-MM-DD hh:mm:ss.ffffff” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT
  to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────────┐
│ to_start_of_ten_minutes('2023-11-12 09:38:18.165575') │
│                       Timestamp                       │
├───────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                   │
└───────────────────────────────────────────────────────┘
```
