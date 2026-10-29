---
title: ST_Y (Lakehouse v2)
description: ST_Y — devolve a coordenada Y (latitude) de uma geometria de ponto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

Devolve a coordenada Y (latitude) de uma geometria de ponto.

## Sintaxe do Analyze

```python
func.st_y(<point>)
```

## Exemplos do Analyze

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## Sintaxe SQL

```sql
ST_Y(<point>)
```

## Exemplos SQL

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
