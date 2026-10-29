---
title: H3_TO_GEO (Lakehouse v1)
description: H3_TO_GEO — renvoie la longitude et la latitude correspondant à l'index H3 donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-geo.md
---

Renvoie la longitude et la latitude correspondant à l'index [H3](https://eng.uber.com/h3/) donné.

## Syntaxe Analyze

```python
func.h3_to_geo(h3)
```

## Exemples Analyze

```python
func.h3_to_geo(644325524701193974)

┌────────────────────────────────────────┐
│   func.h3_to_geo(644325524701193974)   │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_TO_GEO(h3)
```

## Exemples SQL

```sql
SELECT H3_TO_GEO(644325524701193974);

┌────────────────────────────────────────┐
│      h3_to_geo(644325524701193974)     │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```
