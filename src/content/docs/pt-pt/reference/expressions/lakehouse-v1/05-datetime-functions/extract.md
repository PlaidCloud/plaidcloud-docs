---
title: EXTRACT (Lakehouse v1)
description: EXTRACT — obtém a parte indicada de uma data, hora ou carimbo de data/hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/extract.md
---

Obtém a parte indicada de uma data, hora ou carimbo de data/hora.

Ver também: [DATE_PART](../date-part)

## Sintaxe SQL

```sql
EXTRACT( YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | DOW | DOY FROM <date_or_time_expr> )
```

- DOW: dia da semana.
- DOY: dia do ano.

## Tipo de retorno

Número inteiro.

## Exemplos SQL

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
