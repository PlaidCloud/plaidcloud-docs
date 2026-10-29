---
title: UUID (Lakehouse v2)
description: UUID — Devuelve una cadena UUID aleatoria.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

Devuelve una cadena UUID aleatoria.

## Sintaxis de Analyze

```python
func.uuid()
```

## Ejemplos de Analyze

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
UUID()
```

## Ejemplos de SQL

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
