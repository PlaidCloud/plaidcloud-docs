---
title: QUARTER (Lakehouse v2)
description: QUARTER – gibt das Quartal des Jahres aus einem Datum zurück (1–4).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

Gibt das Quartal des Jahres aus einem Datum zurück (1–4).

## Analyze-Syntax

```python
func.quarter(<date>)
```

## Analyze-Beispiele

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## SQL-Syntax

```sql
QUARTER(<date>)
```

## SQL-Beispiele

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
