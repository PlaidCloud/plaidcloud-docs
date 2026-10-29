---
title: TO_MONTHS (Lakehouse v1)
description: TO_MONTHS – wandelt eine angegebene Anzahl von Monaten in den Typ Interval um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-months.md
---

Wandelt eine angegebene Anzahl von Monaten in den Typ Interval um.

- Akzeptiert positive Ganzzahlen, null und negative Ganzzahlen als Eingabe.

## Analyze-Syntax

```python
func.to_months(<months>)
```

## Analyze-Beispiele

```python
func.to_months(2)
┌──────────────────────────────────────────────────────┐
│ func.to_months(2)                                    │
├──────────────────────────────────────────────────────┤
│ 2 months                                             │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_MONTHS(<months>)
```

## Rückgabetyp

Interval (in Monaten dargestellt).

## SQL-Beispiele

```sql
SELECT TO_MONTHS(2), TO_MONTHS(0), TO_MONTHS((- 2));

┌──────────────────────────────────────────────┐
│ to_months(2) │ to_months(0) │ to_months(- 2) │
├──────────────┼──────────────┼────────────────┤
│ 2 months     │ 00:00:00     │ -2 months      │
└──────────────────────────────────────────────┘
```
