---
title: CATALOG (Lakehouse v2)
description: CATALOG — zwraca nazwę bieżącego katalogu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

Zwraca nazwę bieżącego katalogu.

## Składnia Analyze

```python
func.catalog()
```

## Przykłady Analyze

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## Składnia SQL

```sql
CATALOG()
```

## Przykłady SQL

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
