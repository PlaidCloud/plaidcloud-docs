---
title: SKEWNESS (Lakehouse v1)
description: SKEWNESS – gibt die Schiefe (Asymmetrie der Verteilung) aller Eingabewerte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

Aggregatfunktion.

Die Funktion `SKEWNESS()` gibt die Schiefe aller Eingabewerte zurück.

## Analyze-Syntax

```python
func.skewness(<expr>)
```

## Analyze-Beispiele

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## SQL-Syntax

```sql
SKEWNESS(<expr>)
```

## Argumente

| Argumente | Beschreibung                    |
|-----------| -----------                     |
| `<expr>`  | Beliebiger numerischer Ausdruck |

## Rückgabetyp

Nullable Float64.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
```sql
CREATE TABLE temperature_data (
                                  id INT,
                                  city_id INT,
                                  temperature FLOAT
);

INSERT INTO temperature_data (id, city_id, temperature)
VALUES (1, 1, 60),
       (2, 1, 65),
       (3, 1, 62),
       (4, 2, 70),
       (5, 2, 75);
```

**Abfragedemo: Schiefe der Temperaturdaten berechnen**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**Ergebnis**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
