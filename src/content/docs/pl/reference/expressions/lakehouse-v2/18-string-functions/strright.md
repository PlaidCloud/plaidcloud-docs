---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT — zwraca N ostatnich znaków od prawej strony ciągu. Alias funkcji `RIGHT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

Zwraca N ostatnich znaków od prawej strony ciągu. Alias funkcji `RIGHT`.

## Składnia Analyze

```python
func.strright(<str>, <len>)
```

## Przykłady Analyze

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Składnia SQL

```sql
STRRIGHT(<str>, <len>)
```

## Przykłady SQL

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
