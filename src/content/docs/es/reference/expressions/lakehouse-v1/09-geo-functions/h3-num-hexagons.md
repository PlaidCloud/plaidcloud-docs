---
title: H3_NUM_HEXAGONS (Lakehouse v1)
description: H3_NUM_HEXAGONS — devuelve el número de índices H3 únicos para la resolución dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

Devuelve el número de índices [H3](https://eng.uber.com/h3/) únicos para la resolución dada. 

## Sintaxis de Analyze

```python
func.h3_num_hexagons(res)
```

## Ejemplos de Analyze

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_NUM_HEXAGONS(res)
```

## Ejemplos de SQL

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
