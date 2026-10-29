---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID (Lakehouse v1)
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — determina se o H3Index fornecido é uma aresta unidirecional válida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

Determina se o H3Index fornecido é um índice de aresta unidirecional válido. Devolve 1 se for uma aresta unidirecional e 0 caso contrário.

## Sintaxe do Analyze

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Exemplos do Analyze

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## Exemplos de SQL

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
