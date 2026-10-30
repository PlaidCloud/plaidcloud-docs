---
title: TIMESTAMP_DIFF (Lakehouse v1)
description: TIMESTAMP_DIFF – berechnet die Differenz zwischen zwei Zeitstempeln und gibt das Ergebnis als INTERVAL zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

Berechnet die Differenz zwischen zwei Zeitstempeln und gibt das Ergebnis als INTERVAL zurück.

## Analyze-Syntax

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Analyze-Beispiele

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## Rückgabetyp

INTERVAL (formatiert als `hours:minutes:seconds`).

## SQL-Beispiele

Dieses Beispiel zeigt, dass die Zeitdifferenz zwischen dem 1. Februar 2025 und dem 1. Januar 2025 744 Stunden beträgt, was 31 Tagen entspricht:

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
