---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — zwraca szczegółowe informacje o użyciu pamięci.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

Zwraca szczegółowe informacje o użyciu pamięci.

## Składnia Analyze

```python
func.inspect_memory_detail()
```

## Przykłady Analyze

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## Składnia SQL

```sql
INSPECT_MEMORY_DETAIL()
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
