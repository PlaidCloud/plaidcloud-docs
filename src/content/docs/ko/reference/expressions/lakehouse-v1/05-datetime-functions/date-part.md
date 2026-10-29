---
title: DATE_PART (Lakehouse v1)
description: DATE_PART — 날짜, 시간 또는 타임스탬프에서 지정한 부분을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-part.md
---

날짜, 시간 또는 타임스탬프에서 지정한 부분을 가져옵니다.

참고: [EXTRACT](../extract)

## Analyze 구문

```python
func.date_part(<unit>, <date_or_time_expr>)
```

## Analyze 예시

```python
func.now()           |
---------------------+
2023-10-16 02:09:28.0|

func.date_part('day', now())

func.date_part('day', now())|
----------------------------+
                         16 |
```

## SQL 구문

```sql
DATE_PART( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY, <date_or_time_expr> )
```

- DOW: 요일.
- DOY: 연중 일차.

## 반환 형식

정수입니다.

## SQL 예시

```sql
SELECT NOW();

now()                |
---------------------+
2023-10-16 02:09:28.0|

SELECT DATE_PART(DAY, NOW());

date_part(day, now())|
---------------------+
                   16|

-- October 16, 2023, is a Monday
SELECT DATE_PART(DOW, NOW());

date_part(dow, now())|
---------------------+
                    1|

-- October 16, 2023, is the 289th day of the year
SELECT DATE_PART(DOY, NOW());

date_part(doy, now())|
---------------------+
                  289|

SELECT DATE_PART(MONTH, TO_DATE('2022-05-13'));

date_part(month, to_date('2022-05-13'))|
---------------------------------------+
                                      5|
```
