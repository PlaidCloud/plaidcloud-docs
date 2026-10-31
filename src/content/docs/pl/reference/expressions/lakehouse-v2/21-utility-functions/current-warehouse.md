---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE — zwraca nazwę bieżącego magazynu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

Zwraca nazwę bieżącego magazynu.

## Składnia Analyze

```python
func.current_warehouse()
```

## Przykłady Analyze

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## Składnia SQL

```sql
CURRENT_WAREHOUSE()
```

## Przykłady SQL

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
