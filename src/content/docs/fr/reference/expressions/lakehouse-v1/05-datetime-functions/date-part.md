---
title: DATE_PART (Lakehouse v1)
description: DATE_PART — extrait la partie indiquée d'une date, d'une heure ou d'un horodatage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-part.md
---

Extrait la partie indiquée d'une date, d'une heure ou d'un horodatage.

Voir aussi : [EXTRACT](../extract)

## Syntaxe Analyze

```python
func.date_part(<unit>, <date_or_time_expr>)
```

## Exemples Analyze

```python
func.now()           |
---------------------+
2023-10-16 02:09:28.0|

func.date_part('day', now())

func.date_part('day', now())|
----------------------------+
                         16 |
```

## Syntaxe SQL

```sql
DATE_PART( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY, <date_or_time_expr> )
```

- DOW : jour de la semaine.
- DOY : jour de l'année.

## Type de retour

Entier.

## Exemples SQL

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
