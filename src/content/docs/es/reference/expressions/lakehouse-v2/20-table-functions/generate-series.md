---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — Genera una serie de valores desde un inicio hasta un final con un paso dado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

Genera una serie de valores desde un inicio hasta un final con un paso dado.

## Sintaxis de Analyze

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Ejemplos de Analyze

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## Sintaxis de SQL

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(GENERATE_SERIES(1, 5));

┌───────────┐
│ 1
2
3
4
5  │
└───────────┘
```
