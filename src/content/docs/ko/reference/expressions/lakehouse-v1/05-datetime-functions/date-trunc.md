---
title: DATE_TRUNC (Lakehouse v1)
description: DATE_TRUNC — 날짜, 시간 또는 타임스탬프 값을 지정한 정밀도로 자릅니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

날짜, 시간 또는 타임스탬프 값을 지정한 정밀도로 자릅니다. 예를 들어 `2022-07-07`을 `MONTH`로 자르면 결과는 `2022-07-01`이고, `2022-07-07 01:01:01.123456`을 `SECOND`로 자르면 결과는 `2022-07-07 01:01:01.000000`입니다.

## Analyze 구문

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Analyze 예시

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## 인수

| 인수             | 설명                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | 다음 값 중 하나여야 합니다. `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`  |
| `<date_or_time_expr>` | `DATE` 또는 `TIMESTAMP` 형식의 값                                                              |

## 반환 형식

`<date_or_time_expr>` 인수와 같은 형식의 값을 반환합니다.

## SQL 예시

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
