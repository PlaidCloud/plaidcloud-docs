---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — dodaje określony przedział czasu do daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

Dodaje określony przedział czasu do daty i godziny.

## Składnia Analyze

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Przykłady Analyze

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Składnia SQL

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## Przykłady SQL

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
