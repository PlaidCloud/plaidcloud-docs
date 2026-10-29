---
title: DATE_PART（Lakehouse v1）
description: DATE_PART——检索日期、时间或时间戳的指定部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-part.md
---

检索日期、时间或时间戳的指定部分。

另请参阅：[EXTRACT](../extract)

## Analyze 语法

```python
func.date_part(<unit>, <date_or_time_expr>)
```

## Analyze 示例

```python
func.now()           |
---------------------+
2023-10-16 02:09:28.0|

func.date_part('day', now())

func.date_part('day', now())|
----------------------------+
                         16 |
```

## SQL 语法

```sql
DATE_PART( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY, <date_or_time_expr> )
```

- DOW：星期几。
- DOY：一年中的第几天。

## 返回类型

整数。

## SQL 示例

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
