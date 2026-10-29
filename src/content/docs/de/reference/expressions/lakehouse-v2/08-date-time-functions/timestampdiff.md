---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF – gibt die Differenz zwischen zwei Datumswerten mit Uhrzeit in der angegebenen Einheit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

Gibt die Differenz zwischen zwei Datumswerten mit Uhrzeit in der angegebenen Einheit zurück.

## Analyze-Syntax

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Analyze-Beispiele

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL-Syntax

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## SQL-Beispiele

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
