---
title: H3_TO_GEO (Lakehouse v1)
description: H3_TO_GEO — devuelve la longitud y la latitud correspondientes al índice H3 dado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-geo.md
---

Devuelve la longitud y la latitud correspondientes al índice [H3](https://eng.uber.com/h3/) dado. 

## Sintaxis de Analyze

```python
func.h3_to_geo(h3)
```

## Ejemplos de Analyze

```python
func.h3_to_geo(644325524701193974)

┌────────────────────────────────────────┐
│   func.h3_to_geo(644325524701193974)   │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_TO_GEO(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_TO_GEO(644325524701193974);

┌────────────────────────────────────────┐
│      h3_to_geo(644325524701193974)     │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```
