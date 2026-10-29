---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7 — Devuelve una cadena UUID v7 ordenada por tiempo. Los valores UUID v7 se pueden ordenar por hora de creación.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

Devuelve una cadena UUID v7 ordenada por tiempo. Los valores UUID v7 se pueden ordenar por hora de creación.

## Sintaxis de Analyze

```python
func.uuid_v7()
```

## Ejemplos de Analyze

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
UUID_V7()
```

## Ejemplos de SQL

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
