---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — zwraca informacje o wszystkich obiektach pipe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

Zwraca informacje o wszystkich obiektach pipe.

## Składnia Analyze

```python
func.inspect_all_pipes()
```

## Przykłady Analyze

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## Składnia SQL

```sql
INSPECT_ALL_PIPES()
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
