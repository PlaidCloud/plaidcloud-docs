---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC — Devuelve un UUID aleatorio como un valor LARGEINT de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

Devuelve un UUID aleatorio como un valor LARGEINT de 128 bits.

## Sintaxis de Analyze

```python
func.uuid_numeric()
```

## Ejemplos de Analyze

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Sintaxis de SQL

```sql
UUID_NUMERIC()
```

## Ejemplos de SQL

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
