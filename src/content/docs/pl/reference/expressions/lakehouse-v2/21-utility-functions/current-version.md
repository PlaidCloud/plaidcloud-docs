---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION — zwraca bieżącą wersję StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

Zwraca bieżącą wersję StarRocks.

## Składnia Analyze

```python
func.current_version()
```

## Przykłady Analyze

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## Składnia SQL

```sql
CURRENT_VERSION()
```

## Przykłady SQL

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
