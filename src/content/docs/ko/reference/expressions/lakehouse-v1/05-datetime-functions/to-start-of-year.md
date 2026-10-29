---
title: TO_START_OF_YEAR (Lakehouse v1)
description: TO_START_OF_YEAR — 날짜 또는 시간이 포함된 날짜의 해 첫날을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-year.md
---

날짜 또는 시간이 포함된 날짜(timestamp/datetime)의 해 첫날을 반환합니다.

## Analyze 구문

```python
func.to_start_of_year(<expr>)
```

## Analyze 예제

```python
func.to_start_of_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_year('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_START_OF_YEAR(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 반환 형식

`DATE`, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT
  to_start_of_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_year('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-01-01                                     │
└────────────────────────────────────────────────┘
```
