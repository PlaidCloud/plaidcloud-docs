---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — cria uma geometria de círculo a partir da longitude e da latitude do centro e de um raio em metros.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

Cria uma geometria de círculo a partir da longitude e da latitude do centro e de um raio em metros.

## Sintaxe de Analyze

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Exemplos de Analyze

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxe SQL

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## Exemplos SQL

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
