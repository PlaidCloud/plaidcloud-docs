---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — retorna o índice H3 da célula hexagonal onde fica a localização informada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

Retorna o índice [H3](https://eng.uber.com/h3/) da célula hexagonal onde fica a localização informada. Um retorno igual a 0 significa que ocorreu um erro.

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
