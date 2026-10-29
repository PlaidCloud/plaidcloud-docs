---
title: ST_X (Lakehouse v2)
description: ST_X — Retorna a coordenada X (longitude) de uma geometria de ponto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

Retorna a coordenada X (longitude) de uma geometria de ponto.

## Sintaxe do Analyze

```python
func.st_x(<point>)
```

## Exemplos do Analyze

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## Sintaxe SQL

```sql
ST_X(<point>)
```

## Exemplos de SQL

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
