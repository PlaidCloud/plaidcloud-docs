---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD – addiert ein angegebenes Zeitintervall zu einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

Addiert ein angegebenes Zeitintervall zu einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Analyze-Beispiele

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL-Syntax

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## SQL-Beispiele

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
