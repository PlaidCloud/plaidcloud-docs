---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — analizuje ciąg znaków do daty przy użyciu ciągu formatu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

Analizuje ciąg znaków do daty przy użyciu ciągu formatu.

## Składnia Analyze

```python
func.str_to_date(<str>, <format>)
```

## Przykłady Analyze

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
STR_TO_DATE(<str>, <format>)
```

## Przykłady SQL

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
