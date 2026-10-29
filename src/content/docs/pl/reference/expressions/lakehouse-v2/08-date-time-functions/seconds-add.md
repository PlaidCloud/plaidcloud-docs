---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — dodaje określoną liczbę sekund do daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

Dodaje określoną liczbę sekund do daty i godziny.

## Składnia Analyze

```python
func.seconds_add(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## Składnia SQL

```sql
SECONDS_ADD(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
