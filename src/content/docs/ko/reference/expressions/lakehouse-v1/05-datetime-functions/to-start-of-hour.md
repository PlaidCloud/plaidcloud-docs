---
title: TO_START_OF_HOUR (Lakehouse v1)
description: TO_START_OF_HOUR — 날짜/시간(타임스탬프/datetime)을 해당 시의 시작 시점으로 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-hour.md
---

날짜/시간(타임스탬프/datetime)을 해당 시의 시작 시점으로 내림합니다.

## Analyze 구문

```python
func.to_start_of_hour(<expr>)
```

## Analyze 예시

```python
func.to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_hour('2023-11-12 09:38:18.165575')            │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_START_OF_HOUR(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr>`  | 타임스탬프   |

## 반환 형식

`TIMESTAMP`이며, “YYYY-MM-DD hh:mm:ss.ffffff” 형식의 날짜를 반환합니다.

## SQL 예시

```sql
SELECT
  to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_hour('2023-11-12 09:38:18.165575') │
│                    Timestamp                   │
├────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                            │
└────────────────────────────────────────────────┘
```
