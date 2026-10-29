---
title: MONTHS_BETWEEN (Lakehouse v1)
description: MONTHS_BETWEEN – gibt die Anzahl der Monate zwischen date1 und date2 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/months-between.md
---

Gibt die Anzahl der Monate zwischen *date1* und *date2* zurück.

## Analyze-Syntax

```python
func.months_between(<date1>, <date2>)
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
MONTHS_BETWEEN( <date1>, <date2> )
```

## Argumente

*date1* und *date2* können vom Typ DATE, vom Typ TIMESTAMP oder eine Mischung aus beiden sein.

## Rückgabetyp

Die Funktion gibt einen FLOAT-Wert nach den folgenden Regeln zurück:

- Liegt *date1* vor *date2*, gibt die Funktion einen negativen Wert zurück, andernfalls einen positiven Wert.

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

- Fallen *date1* und *date2* auf denselben Tag ihres jeweiligen Monats oder sind beide der letzte Tag ihres jeweiligen Monats, ist das Ergebnis eine Ganzzahl. Andernfalls berechnet die Funktion den gebrochenen Anteil des Ergebnisses auf Grundlage eines Monats mit 31 Tagen.

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

- Sind *date1* und *date2* dasselbe Datum, ignoriert die Funktion alle Zeitanteile und gibt 0 zurück.

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
