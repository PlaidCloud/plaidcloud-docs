---
title: TO_HOURS (Lakehouse v1)
description: TO_HOURS – wandelt eine angegebene Anzahl von Stunden in den Typ Interval um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-hours.md
---

Wandelt eine angegebene Anzahl von Stunden in den Typ Interval um.

- Akzeptiert positive Ganzzahlen, null und negative Ganzzahlen als Eingabe.

## Analyze-Syntax

```python
func.to_hours(<hours>)
```

## Analyze-Beispiele

```python
func.to_hours(2)
┌──────────────────────────────────────────────────────┐
│ func.to_hours(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2:00:00                                              │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_HOURS(<hours>)
```

## Rückgabetyp

Interval (im Format `hh:mm:ss`).

## SQL-Beispiele

```sql
SELECT TO_HOURS(2), TO_HOURS(0), TO_HOURS((- 2));

┌───────────────────────────────────────────┐
│ to_hours(2) │ to_hours(0) │ to_hours(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2:00:00     │ 00:00:00    │ -2:00:00      │
└───────────────────────────────────────────┘
```
