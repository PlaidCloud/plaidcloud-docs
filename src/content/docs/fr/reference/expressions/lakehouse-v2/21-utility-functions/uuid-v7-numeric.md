---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC — renvoie un UUID v7 ordonné dans le temps sous la forme d'une valeur LARGEINT de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

Renvoie un UUID v7 ordonné dans le temps sous la forme d'une valeur LARGEINT de 128 bits. Les valeurs UUID v7 peuvent être triées selon leur date de création.

## Syntaxe Analyze

```python
func.uuid_v7_numeric()
```

## Exemples Analyze

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
UUID_V7_NUMERIC()
```

## Exemples SQL

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
