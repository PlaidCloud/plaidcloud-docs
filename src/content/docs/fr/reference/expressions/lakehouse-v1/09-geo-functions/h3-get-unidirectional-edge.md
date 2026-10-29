---
title: H3_GET_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_UNIDIRECTIONAL_EDGE — renvoie l'arête entre les deux index H3 donnés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge.md
---

Renvoie l'arête entre les deux index [H3](https://eng.uber.com/h3/) donnés.

## Syntaxe Analyze

```python
func.h3_get_unidirectional_edge(h3, a_h3)
```

## Exemples Analyze

```python
func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754)

┌─────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├─────────────────────────────────────────────────────────────────────────┤
│                                                     1581074247194257065 │
└─────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_GET_UNIDIRECTIONAL_EDGE(h3, a_h3)
```

## Exemples SQL

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE(644325524701193897, 644325524701193754);

┌────────────────────────────────────────────────────────────────────┐
│ h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├────────────────────────────────────────────────────────────────────┤
│                                                1581074247194257065 │
└────────────────────────────────────────────────────────────────────┘
```
