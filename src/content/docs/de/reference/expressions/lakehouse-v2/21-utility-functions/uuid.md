---
title: UUID (Lakehouse v2)
description: UUID — gibt eine zufällige UUID als Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

Gibt eine zufällige UUID als Zeichenfolge zurück.

## Analyze-Syntax

```python
func.uuid()
```

## Analyze-Beispiele

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## SQL-Syntax

```sql
UUID()
```

## SQL-Beispiele

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
