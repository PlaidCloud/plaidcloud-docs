---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — konwertuje wartość VARCHAR na wartość DATE zgodnie z ciągiem formatu Teradata.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Konwertuje wartość VARCHAR na wartość DATE zgodnie z ciągiem formatu Teradata.

## Składnia Analyze

```python
func.to_tera_date(<str>, <format>)
```

## Przykłady Analyze

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
TO_TERA_DATE(<str>, <format>)
```

## Przykłady SQL

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
