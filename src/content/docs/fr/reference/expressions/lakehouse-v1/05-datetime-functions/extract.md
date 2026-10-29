---
title: EXTRACT (Lakehouse v1)
description: EXTRACT — extrait la partie indiquée d'une date, d'une heure ou d'un horodatage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/extract.md
---

Extrait la partie indiquée d'une date, d'une heure ou d'un horodatage.

Voir aussi : [DATE_PART](../date-part)

## Syntaxe SQL

```sql
EXTRACT( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY FROM <date_or_time_expr> )
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
