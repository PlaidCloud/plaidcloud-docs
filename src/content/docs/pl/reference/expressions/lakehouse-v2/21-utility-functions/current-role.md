---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — zwraca bieżącą aktywną rolę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

Zwraca bieżącą aktywną rolę.

## Składnia Analyze

```python
func.current_role()
```

## Przykłady Analyze

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## Składnia SQL

```sql
CURRENT_ROLE()
```

## Przykłady SQL

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
