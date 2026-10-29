---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID (Lakehouse v1)
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — determina si el H3Index proporcionado es una arista unidireccional válida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

Determina si el H3Index proporcionado es un índice de arista unidireccional válido. Devuelve 1 si es una arista unidireccional y 0 en caso contrario.

## Sintaxis de Analyze

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Ejemplos de Analyze

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
