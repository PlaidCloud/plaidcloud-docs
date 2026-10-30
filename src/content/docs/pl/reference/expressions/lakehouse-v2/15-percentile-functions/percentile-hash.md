---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — oblicza stan percentyla na podstawie wartości liczbowej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

Oblicza stan percentyla na podstawie wartości liczbowej.

## Składnia Analyze

```python
func.percentile_hash(<value>)
```

## Przykłady Analyze

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## Składnia SQL

```sql
PERCENTILE_HASH(<value>)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
