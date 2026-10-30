---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY – gibt den letzten Tag des angegebenen Intervalls (Woche, Monat, Quartal oder Jahr) zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

Gibt anhand des angegebenen Datums oder Zeitstempels den letzten Tag des angegebenen Intervalls (Woche, Monat, Quartal oder Jahr) zurück.

## Analyze-Syntax

```python
func.last_day(<date_expression>, <interval>)
```

## Analyze-Beispiele

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
LAST_DAY(<date_expression>, <interval>)
```

| Parameter           | Beschreibung                                                                                                  |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Ein DATE- oder TIMESTAMP-Wert, für den der letzte Tag des angegebenen Intervalls berechnet wird.              |
| `<interval>`        | Der Intervalltyp, für den der letzte Tag ermittelt wird. Zulässige Werte sind `week`, `month`, `quarter` und `year`. |

## Rückgabetyp

Datum.

## SQL-Beispiele

Angenommen, Sie möchten das Abrechnungsdatum bestimmen, das immer der letzte Tag des Monats ist, ausgehend von einem beliebigen Transaktionsdatum (z. B. 2024-11-13):

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
