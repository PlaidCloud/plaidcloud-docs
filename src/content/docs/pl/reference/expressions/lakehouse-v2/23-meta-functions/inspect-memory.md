---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — zwraca informacje o użyciu pamięci dla bieżącego węzła.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

Zwraca informacje o użyciu pamięci dla bieżącego węzła.

## Składnia Analyze

```python
func.inspect_memory()
```

## Przykłady Analyze

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## Składnia SQL

```sql
INSPECT_MEMORY()
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
