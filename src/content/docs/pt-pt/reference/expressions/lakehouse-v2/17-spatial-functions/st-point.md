---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — cria uma geometria de ponto a partir de valores de longitude e latitude.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

Cria uma geometria de ponto a partir de valores de longitude e latitude.

## Sintaxe do Analyze

```python
func.st_point(<lng>, <lat>)
```

## Exemplos do Analyze

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxe SQL

```sql
ST_POINT(<lng>, <lat>)
```

## Exemplos SQL

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
