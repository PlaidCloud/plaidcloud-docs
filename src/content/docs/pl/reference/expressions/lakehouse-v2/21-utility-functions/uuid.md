---
title: UUID (Lakehouse v2)
description: UUID — zwraca losowy ciąg UUID.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

Zwraca losowy ciąg UUID.

## Składnia Analyze

```python
func.uuid()
```

## Przykłady Analyze

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## Składnia SQL

```sql
UUID()
```

## Przykłady SQL

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
