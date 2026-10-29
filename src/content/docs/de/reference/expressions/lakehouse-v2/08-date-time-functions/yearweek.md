---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK – gibt Jahr und Kalenderwoche eines Datums als Ganzzahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

Gibt Jahr und Kalenderwoche eines Datums als Ganzzahl zurück.

## Analyze-Syntax

```python
func.yearweek(<date>[, <mode>])
```

## Analyze-Beispiele

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## SQL-Syntax

```sql
YEARWEEK(<date>[, <mode>])
```

## SQL-Beispiele

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
