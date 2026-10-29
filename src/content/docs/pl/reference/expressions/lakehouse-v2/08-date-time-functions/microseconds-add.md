---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — dodaje określoną liczbę mikrosekund do daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

Dodaje określoną liczbę mikrosekund do daty i godziny.

## Składnia Analyze

```python
func.microseconds_add(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## Składnia SQL

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
