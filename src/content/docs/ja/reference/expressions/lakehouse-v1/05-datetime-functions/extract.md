---
title: EXTRACT（Lakehouse v1）
description: EXTRACT — 日付、時刻、またはタイムスタンプから指定した部分を取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/extract.md
---

日付、時刻、またはタイムスタンプから指定した部分を取得します。

関連項目：[DATE_PART](../date-part)

## SQL 構文

```sql
EXTRACT( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY FROM <date_or_time_expr> )
```

- DOW：曜日（Day of the Week）。
- DOY：年内通算日（Day of Year）。

## 戻り値の型

整数。

## SQL の例

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
