---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP – gibt die Varianz der Stichprobe zurück. Alias für `VARIANCE_SAMP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

Gibt die Varianz der Stichprobe zurück. Alias für `VARIANCE_SAMP`.

## Analyze-Syntax

```python
func.var_samp(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL-Syntax

```sql
VAR_SAMP(<score>)
```

## SQL-Beispiele

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
