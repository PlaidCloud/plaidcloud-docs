---
title: TIME_SLOT (Lakehouse v1)
description: TIME_SLOT — zaokrągla czas do pełnych pół godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

Zaokrągla czas do pełnych pół godziny.

## Składnia Analyze

```python
func.time_slot(<expr>)
```

## Przykłady Analyze

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## Składnia SQL

```sql
time_slot(<expr>)
```

## Argumenty

| Argumenty   | Opis           |
| ----------- | -------------- |
| `<expr>`    | znacznik czasu |

## Zwracany typ

`TIMESTAMP`, zwracany w formacie „YYYY-MM-DD hh:mm:ss.ffffff”.

## Przykłady SQL

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
