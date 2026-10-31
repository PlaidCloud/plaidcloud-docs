---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID (Lakehouse v1)
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — détermine si l'H3Index fourni est un index d'arête unidirectionnelle valide.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

Détermine si l'H3Index fourni est un index d'arête unidirectionnelle valide. Renvoie 1 s'il s'agit d'une arête unidirectionnelle, 0 sinon.

## Syntaxe Analyze

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Exemples Analyze

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## Exemples SQL

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
