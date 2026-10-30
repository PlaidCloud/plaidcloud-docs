---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7 — renvoie une chaîne UUID v7 ordonnée dans le temps. Les valeurs UUID v7 peuvent être triées selon leur date de création.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

Renvoie une chaîne UUID v7 ordonnée dans le temps. Les valeurs UUID v7 peuvent être triées selon leur date de création.

## Syntaxe Analyze

```python
func.uuid_v7()
```

## Exemples Analyze

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## Syntaxe SQL

```sql
UUID_V7()
```

## Exemples SQL

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
