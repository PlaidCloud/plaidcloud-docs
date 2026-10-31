---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH — sprawdza, czy ciąg zaczyna się od podanego prefiksu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

Sprawdza, czy ciąg zaczyna się od podanego prefiksu.

## Składnia Analyze

```python
func.starts_with(<str>, <prefix>)
```

## Przykłady Analyze

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
STARTS_WITH(<str>, <prefix>)
```

## Przykłady SQL

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
