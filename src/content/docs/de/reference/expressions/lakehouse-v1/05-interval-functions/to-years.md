---
title: TO_YEARS (Lakehouse v1)
description: TO_YEARS – wandelt eine angegebene Anzahl von Jahren in den Typ Interval um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-years.md
---

Wandelt eine angegebene Anzahl von Jahren in den Typ Interval um.

- Akzeptiert positive Ganzzahlen, null und negative Ganzzahlen als Eingabe.

## Analyze-Syntax

```python
func.to_years(<years>)
```

## Analyze-Beispiele

```python
func.to_years(2)
┌──────────────────────────────────────────────────────┐
│ func.to_years(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2 years                                              │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_YEARS(<years>)
```

## Rückgabetyp

Interval (in Jahren dargestellt).

## SQL-Beispiele

```sql
SELECT TO_YEARS(2), TO_YEARS(0), TO_YEARS((- 2));

┌───────────────────────────────────────────┐
│ to_years(2) │ to_years(0) │ to_years(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2 years     │ 00:00:00    │ -2 years      │
└───────────────────────────────────────────┘
```
