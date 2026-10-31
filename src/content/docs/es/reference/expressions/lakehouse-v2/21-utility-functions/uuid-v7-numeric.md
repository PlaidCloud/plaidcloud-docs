---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC — Devuelve un UUID v7 ordenado por tiempo como un valor LARGEINT de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

Devuelve un UUID v7 ordenado por tiempo como un valor LARGEINT de 128 bits. Los valores UUID v7 se pueden ordenar por hora de creación.

## Sintaxis de Analyze

```python
func.uuid_v7_numeric()
```

## Ejemplos de Analyze

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
UUID_V7_NUMERIC()
```

## Ejemplos de SQL

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
