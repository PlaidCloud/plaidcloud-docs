---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7 — retorna uma string UUID v7 ordenada por tempo. Os valores UUID v7 podem ser ordenados pelo momento de criação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

Retorna uma string UUID v7 ordenada por tempo. Os valores UUID v7 podem ser ordenados pelo momento de criação.

## Sintaxe do Analyze

```python
func.uuid_v7()
```

## Exemplos do Analyze

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## Sintaxe SQL

```sql
UUID_V7()
```

## Exemplos de SQL

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
