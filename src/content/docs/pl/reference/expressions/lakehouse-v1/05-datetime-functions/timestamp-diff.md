---
title: TIMESTAMP_DIFF (Lakehouse v1)
description: TIMESTAMP_DIFF — oblicza różnicę między dwoma znacznikami czasu i zwraca wynik jako INTERVAL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

Oblicza różnicę między dwoma znacznikami czasu i zwraca wynik jako INTERVAL.

## Składnia Analyze

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Przykłady Analyze

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## Zwracany typ

INTERVAL (w formacie `hours:minutes:seconds`).

## Przykłady SQL

Ten przykład pokazuje, że różnica czasu między 1 lutego 2025 a 1 stycznia 2025 wynosi 744 godziny, co odpowiada 31 dniom:

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
