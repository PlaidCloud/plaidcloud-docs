---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP – gibt die Varianz der Stichprobe zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

Gibt die Varianz der Stichprobe zurück.

## Analyze-Syntax

```python
func.variance_samp(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL-Syntax

```sql
VARIANCE_SAMP(<score>)
```

## SQL-Beispiele

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
