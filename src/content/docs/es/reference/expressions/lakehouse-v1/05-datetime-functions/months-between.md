---
title: MONTHS_BETWEEN (Lakehouse v1)
description: MONTHS_BETWEEN — devuelve el número de meses entre date1 y date2.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/months-between.md
---

Devuelve el número de meses entre *date1* y *date2*.

## Sintaxis de Analyze

```python
func.months_between(<date1>, <date2>)
```

## Ejemplos de Analyze

```python
func.months_between(func.to_date('2024-03-15'), func.to_date('2024-02-15'))
┌───────────────────────────────────────────────────────────────────────────────┐
│ func.months_between(func.to_date('2024-03-15'), func.to_date('2024-02-15'))   │
├───────────────────────────────────────────────────────────────────────────────┤
│ 1                                                                             │
└───────────────────────────────────────────────────────────────────────────────┘
```

```python
func.months_between(func.to_date('2024-02-15'), func.to_date('2024-03-15'))
┌───────────────────────────────────────────────────────────────────────────────┐
│ func.months_between(func.to_date('2024-02-15'), func.to_date('2024-03-15'))   │
├───────────────────────────────────────────────────────────────────────────────┤
│ -1                                                                             │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
MONTHS_BETWEEN( <date1>, <date2> )
```

## Argumentos

*date1* y *date2* pueden ser de tipo DATE, de tipo TIMESTAMP o una combinación de ambos.

## Tipo de valor devuelto

La función devuelve un valor FLOAT según las reglas siguientes:

- Si *date1* es anterior a *date2*, la función devuelve un valor negativo; de lo contrario, devuelve un valor positivo.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-03-15'::DATE,
                    '2024-02-15'::DATE),
        MONTHS_BETWEEN('2024-02-15'::DATE,
                    '2024-03-15'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-03-15'::date, '2024-02-15'::date): 1
    months_between('2024-02-15'::date, '2024-03-15'::date): -1
    ```

- Si *date1* y *date2* caen en el mismo día de sus respectivos meses, o ambas son el último día de sus respectivos meses, el resultado es un entero. De lo contrario, la función calcula la parte fraccionaria del resultado sobre la base de un mes de 31 días.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-02-29'::DATE,
                    '2024-01-29'::DATE),
        MONTHS_BETWEEN('2024-02-29'::DATE,
                    '2024-01-31'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-02-29'::date, '2024-01-29'::date): 1
    months_between('2024-02-29'::date, '2024-01-31'::date): 1

    SELECT
        MONTHS_BETWEEN('2024-08-05'::DATE,
                    '2024-01-01'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-08-05'::date, '2024-01-01'::date): 7.129032258064516
    ```

- Si *date1* y *date2* son la misma fecha, la función ignora cualquier componente de hora y devuelve 0.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-08-05'::DATE,
                    '2024-08-05'::DATE),
        MONTHS_BETWEEN('2024-08-05 02:00:00'::TIMESTAMP,
                    '2024-08-05 01:00:00'::TIMESTAMP);

    -[ RECORD 1 ]-----------------------------------
                                months_between('2024-08-05'::date, '2024-08-05'::date): 0
    months_between('2024-08-05 02:00:00'::timestamp, '2024-08-05 01:00:00'::timestamp): 0
    ```
