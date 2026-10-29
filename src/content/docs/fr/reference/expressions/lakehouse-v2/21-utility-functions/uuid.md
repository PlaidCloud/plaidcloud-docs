---
title: UUID (Lakehouse v2)
description: UUID — renvoie une chaîne UUID aléatoire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

Renvoie une chaîne UUID aléatoire.

## Syntaxe Analyze

```python
func.uuid()
```

## Exemples Analyze

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
UUID()
```

## Exemples SQL

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
