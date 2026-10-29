---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — devuelve un estado de percentil vacío para la inicialización.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

Devuelve un estado de percentil vacío para la inicialización.

## Sintaxis de Analyze

```python
func.percentile_empty()
```

## Ejemplos de Analyze

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_EMPTY()
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
