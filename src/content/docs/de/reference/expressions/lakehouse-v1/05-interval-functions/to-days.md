---
title: TO_DAYS (Lakehouse v1)
description: TO_DAYS – wandelt eine angegebene Anzahl von Tagen in den Typ Interval um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-days.md
---

Wandelt eine angegebene Anzahl von Tagen in den Typ Interval um.

- Akzeptiert positive Ganzzahlen, null und negative Ganzzahlen als Eingabe.

## Analyze-Syntax

```python
func.to_days(<days>)
```

## Analyze-Beispiele

```python
func.to_days(2)
┌──────────────────────────────────────────────────────┐
│ func.to_days(2)                                      │
├──────────────────────────────────────────────────────┤
│ 200 days                                             │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_DAYS(<days>)
```

## Rückgabetyp

Interval (in Tagen dargestellt).

## SQL-Beispiele

```sql
SELECT TO_DAYS(2), TO_DAYS(0), TO_DAYS(-2);

┌────────────────────────────────────────┐
│ to_days(2) │ to_days(0) │ to_days(- 2) │
├────────────┼────────────┼──────────────┤
│ 2 days     │ 00:00:00   │ -2 days      │
└────────────────────────────────────────┘
```
