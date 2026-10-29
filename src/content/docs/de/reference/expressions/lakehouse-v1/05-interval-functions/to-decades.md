---
title: TO_DECADES (Lakehouse v1)
description: TO_DECADES – wandelt eine angegebene Anzahl von Jahrzehnten in den Typ Interval um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-decades.md
---

Wandelt eine angegebene Anzahl von Jahrzehnten in den Typ Interval um.

- Akzeptiert positive Ganzzahlen, null und negative Ganzzahlen als Eingabe.

## Analyze-Syntax

```python
func.to_decades(<decades>)
```

## Analyze-Beispiele

```python
func.to_decades(2)
┌──────────────────────────────────────────────────────┐
│ func.to_decades(2)                                   │
├──────────────────────────────────────────────────────┤
│ 20 years                                             │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_DECADES(<decades>)
```

## Rückgabetyp

Interval (in Jahren dargestellt).

## SQL-Beispiele

```sql
SELECT TO_DECADES(2), TO_DECADES(0), TO_DECADES((- 2));

┌─────────────────────────────────────────────────┐
│ to_decades(2) │ to_decades(0) │ to_decades(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 20 years      │ 00:00:00      │ -20 years       │
└─────────────────────────────────────────────────┘
```
