---
title: TIME_SLOT (Lakehouse v1)
description: TIME_SLOT — 시간을 30분 단위로 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

시간을 30분 단위로 내림합니다.

## Analyze 구문

```python
func.time_slot(<expr>)
```

## Analyze 예시

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## SQL 구문

```sql
time_slot(<expr>)
```

## 인수

| 인수   | 설명 |
| ----------- | ----------- |
| `<expr>`    | 타임스탬프   |

## 반환 형식

`TIMESTAMP`이며, “YYYY-MM-DD hh:mm:ss.ffffff” 형식으로 반환합니다.

## SQL 예시

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
