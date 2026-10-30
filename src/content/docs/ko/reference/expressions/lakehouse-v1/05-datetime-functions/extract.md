---
title: EXTRACT (Lakehouse v1)
description: EXTRACT — 날짜, 시간 또는 타임스탬프에서 지정한 부분을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/extract.md
---

날짜, 시간 또는 타임스탬프에서 지정한 부분을 가져옵니다.

참고: [DATE_PART](../date-part)

## SQL 구문

```sql
EXTRACT( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY FROM <date_or_time_expr> )
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

SELECT EXTRACT(DAY FROM NOW());

extract(day from now())|
-----------------------+
                     16|

-- October 16, 2023, is a Monday
SELECT EXTRACT(DOW FROM NOW());

extract(dow from now())|
-----------------------+
                      1|

-- October 16, 2023, is the 289th day of the year
SELECT EXTRACT(DOY FROM NOW());

extract(doy from now())|
-----------------------+
                    289|

SELECT EXTRACT(MONTH FROM TO_DATE('2022-05-13'));

extract(month from to_date('2022-05-13'))|
-----------------------------------------+
                                        5|
```
