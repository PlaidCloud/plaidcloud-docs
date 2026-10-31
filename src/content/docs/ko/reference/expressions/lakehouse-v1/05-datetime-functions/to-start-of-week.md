---
title: TO_START_OF_WEEK (Lakehouse v1)
description: TO_START_OF_WEEK — 날짜 또는 시간이 포함된 날짜의 주 첫날을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

날짜 또는 시간이 포함된 날짜(timestamp/datetime)의 주 첫날을 반환합니다.
주의 첫날은 일요일 또는 월요일일 수 있으며, `mode` 인수로 지정합니다.

## Analyze 구문

```python
func.to_start_of_week(<expr>)
```

## Analyze 예제

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## 인수

| 인수 | 설명 |
|-----------|-----------------------------------------------------------------------------------------------------|
| `<expr>`  | date/timestamp                                                                                      |
| `[mode]`  | 선택 사항입니다. 0이면 결과는 일요일이고, 그 외의 값이면 결과는 월요일입니다. 기본값은 0입니다. |

## 반환 형식

`DATE`, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT
  to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_week('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-11-12                                     │
└────────────────────────────────────────────────┘
```
