---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP gibt die Stichprobenkovarianz für zwei Ausdrücke zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

Gibt die Stichprobenkovarianz für zwei Ausdrücke zurück.

## Analyze-Syntax

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze-Beispiele

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## SQL-Syntax

```sql
COVAR_SAMP(<y>, <x>)
```

## SQL-Beispiele

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
