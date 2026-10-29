---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP – gibt die Standardabweichung der Stichprobe zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

Gibt die Standardabweichung der Stichprobe zurück.

## Analyze-Syntax

```python
func.stddev_samp(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## SQL-Syntax

```sql
STDDEV_SAMP(<score>)
```

## SQL-Beispiele

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
