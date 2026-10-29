---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — renvoie l'index H3 de la cellule hexagonale dans laquelle se trouve la position donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

Renvoie l'index [H3](https://eng.uber.com/h3/) de la cellule hexagonale dans laquelle se trouve la position donnée. Une valeur renvoyée de 0 signale qu'une erreur s'est produite.

## Syntaxe Analyze

```python
func.geo_to_h3(lon, lat, res)
```

## Exemples Analyze

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
GEO_TO_H3(lon, lat, res)
```

## Exemples SQL

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
