---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD – addiert das Zeit- oder Datumsintervall zum angegebenen Datum bzw. Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

Addiert das Zeit- oder Datumsintervall zum angegebenen Datum bzw. Datum mit Uhrzeit (Timestamp/Datetime).

## Analyze-Syntax

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Analyze-Beispiele

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## Argumente

| Argumente             | Beschreibung                                                                                                      |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Muss einer der folgenden Werte sein: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` und `SECOND`             |
| `<value>`             | Die Anzahl der Zeiteinheiten, die Sie addieren möchten. Wenn Sie beispielsweise 2 Tage addieren möchten, ist dies 2. |
| `<date_or_time_expr>` | Ein Wert vom Typ `DATE` oder `TIMESTAMP`                                                                          |

## Rückgabetyp

Die Funktion gibt einen Wert desselben Typs wie das Argument `<date_or_time_expr>` zurück.

## SQL-Beispiele

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
