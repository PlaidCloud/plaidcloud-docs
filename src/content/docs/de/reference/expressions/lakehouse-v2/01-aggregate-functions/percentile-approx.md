---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX – gibt mit dem t-Digest-Algorithmus einen näherungsweise berechneten Perzentilwert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

Gibt mit dem t-Digest-Algorithmus einen näherungsweise berechneten Perzentilwert zurück.

## Analyze-Syntax

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Analyze-Beispiele

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## SQL-Syntax

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
