---
title: TO_MILLENNIA (Lakehouse v1)
description: TO_MILLENNIA – wandelt eine angegebene Anzahl von Jahrtausenden in den Typ Interval um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-millennia.md
---

Wandelt eine angegebene Anzahl von Jahrtausenden in den Typ Interval um.

- Akzeptiert positive Ganzzahlen, null und negative Ganzzahlen als Eingabe.

## Analyze-Syntax

```python
func.to_millennia(<millennia>)
```

## Analyze-Beispiele

```python
func.to_millennia(2)
┌──────────────────────────────────────────────────────┐
│ func.to_millennia(2)                                 │
├──────────────────────────────────────────────────────┤
│ 2000 years                                            │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_MILLENNIA(<millennia>)
```

## Rückgabetyp

Interval (in Jahren dargestellt).

## SQL-Beispiele

```sql
SELECT TO_MILLENNIA(2), TO_MILLENNIA(0), TO_MILLENNIA((- 2));

┌───────────────────────────────────────────────────────┐
│ to_millennia(2) │ to_millennia(0) │ to_millennia(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 2000 years      │ 00:00:00        │ -2000 years       │
└───────────────────────────────────────────────────────┘
```
