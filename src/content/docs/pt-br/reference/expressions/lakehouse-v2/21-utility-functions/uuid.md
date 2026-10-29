---
title: UUID (Lakehouse v2)
description: UUID — retorna uma string UUID aleatória.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

Retorna uma string UUID aleatória.

## Sintaxe do Analyze

```python
func.uuid()
```

## Exemplos do Analyze

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
UUID()
```

## Exemplos de SQL

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
