---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — calcula un estado de percentil a partir de un valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

Calcula un estado de percentil a partir de un valor numérico.

## Sintaxis de Analyze

```python
func.percentile_hash(<value>)
```

## Ejemplos de Analyze

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_HASH(<value>)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
