---
title: DATE_TRUNC (Lakehouse v1)
description: DATE_TRUNC – kürzt einen Datums-, Zeit- oder Zeitstempelwert auf eine angegebene Genauigkeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

Kürzt einen Datums-, Zeit- oder Zeitstempelwert auf eine angegebene Genauigkeit. Kürzen Sie beispielsweise `2022-07-07` auf `MONTH`, lautet das Ergebnis `2022-07-01`; kürzen Sie `2022-07-07 01:01:01.123456` auf `SECOND`, lautet das Ergebnis `2022-07-07 01:01:01.000000`.

## Analyze-Syntax

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Analyze-Beispiele

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## Argumente

| Argumente             | Beschreibung                                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | Muss einer der folgenden Werte sein: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` und `SECOND`  |
| `<date_or_time_expr>` | Ein Wert vom Typ `DATE` oder `TIMESTAMP`                                                           |

## Rückgabetyp

Die Funktion gibt einen Wert desselben Typs wie das Argument `<date_or_time_expr>` zurück.

## SQL-Beispiele

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
