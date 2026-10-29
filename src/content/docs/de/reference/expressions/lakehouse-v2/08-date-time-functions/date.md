---
title: DATE (Lakehouse v2)
description: DATE – extrahiert den Datumsanteil aus einem Datums-/Zeitausdruck.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

Extrahiert den Datumsanteil aus einem Datums-/Zeitausdruck.

## Analyze-Syntax

```python
func.date(<datetime>)
```

## Analyze-Beispiele

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
DATE(<datetime>)
```

## SQL-Beispiele

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
