---
title: DATE (Lakehouse v2)
description: DATE — wyodrębnia część daty z wyrażenia typu data i godzina.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

Wyodrębnia część daty z wyrażenia typu data i godzina.

## Składnia Analyze

```python
func.date(<datetime>)
```

## Przykłady Analyze

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
DATE(<datetime>)
```

## Przykłady SQL

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
