---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — zwraca pusty stan percentyla do inicjalizacji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

Zwraca pusty stan percentyla do inicjalizacji.

## Składnia Analyze

```python
func.percentile_empty()
```

## Przykłady Analyze

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## Składnia SQL

```sql
PERCENTILE_EMPTY()
```

## Przykłady SQL

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
