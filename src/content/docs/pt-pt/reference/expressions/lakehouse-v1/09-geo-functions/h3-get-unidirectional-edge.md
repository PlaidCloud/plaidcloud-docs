---
title: H3_GET_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_UNIDIRECTIONAL_EDGE — devolve a aresta entre os dois índices H3 indicados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge.md
---

Devolve a aresta entre os dois índices [H3](https://eng.uber.com/h3/) indicados.

## Sintaxe do Analyze

```python
func.h3_get_unidirectional_edge(h3, a_h3)
```

## Exemplos do Analyze

```python
func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754)

┌─────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├─────────────────────────────────────────────────────────────────────────┤
│                                                     1581074247194257065 │
└─────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_GET_UNIDIRECTIONAL_EDGE(h3, a_h3)
```

## Exemplos de SQL

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE(644325524701193897, 644325524701193754);

┌────────────────────────────────────────────────────────────────────┐
│ h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├────────────────────────────────────────────────────────────────────┤
│                                                1581074247194257065 │
└────────────────────────────────────────────────────────────────────┘
```
