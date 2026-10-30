---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — devolve o índice H3 da célula hexagonal onde se encontra a localização indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

Devolve o índice [H3](https://eng.uber.com/h3/) da célula hexagonal onde se encontra a localização indicada. Se devolver 0, ocorreu um erro.

## Sintaxe do Analyze

```python
func.geo_to_h3(lon, lat, res)
```

## Exemplos do Analyze

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
GEO_TO_H3(lon, lat, res)
```

## Exemplos de SQL

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
