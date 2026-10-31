---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT — formatuje wartość daty lub daty i godziny zgodnie z ciągiem formatu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

Formatuje wartość daty lub daty i godziny zgodnie z ciągiem formatu.

## Składnia Analyze

```python
func.date_format(<date>, <format>)
```

## Przykłady Analyze

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Składnia SQL

```sql
DATE_FORMAT(<date>, <format>)
```

## Przykłady SQL

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
