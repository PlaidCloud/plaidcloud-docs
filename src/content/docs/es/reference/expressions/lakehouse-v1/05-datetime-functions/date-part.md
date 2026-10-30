---
title: DATE_PART (Lakehouse v1)
description: DATE_PART — obtiene la parte indicada de una fecha, hora o marca de tiempo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-part.md
---

Obtiene la parte indicada de una fecha, hora o marca de tiempo.

Consulte también: [EXTRACT](../extract)

## Sintaxis de Analyze

```python
func.date_part(<unit>, <date_or_time_expr>)
```

## Ejemplos de Analyze

```python
func.now()           |
---------------------+
2023-10-16 02:09:28.0|

func.date_part('day', now())

func.date_part('day', now())|
----------------------------+
                         16 |
```

## Sintaxis de SQL

```sql
DATE_PART( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY, <date_or_time_expr> )
```

- DOW: Día de la semana.
- DOY: Día del año.

## Tipo de valor devuelto

Entero.

## Ejemplos de SQL

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
