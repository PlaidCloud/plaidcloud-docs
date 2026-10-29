---
title: H3_GET_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_UNIDIRECTIONAL_EDGE — gibt die Kante zwischen den beiden angegebenen H3-Indizes zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge.md
---

Gibt die Kante zwischen den beiden angegebenen [H3](https://eng.uber.com/h3/)-Indizes zurück.

## Analyze-Syntax

```python
func.h3_get_unidirectional_edge(h3, a_h3)
```

## Analyze-Beispiele

```python
func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754)

┌─────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├─────────────────────────────────────────────────────────────────────────┤
│                                                     1581074247194257065 │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_GET_UNIDIRECTIONAL_EDGE(h3, a_h3)
```

## SQL-Beispiele

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE(644325524701193897, 644325524701193754);

┌────────────────────────────────────────────────────────────────────┐
│ h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├────────────────────────────────────────────────────────────────────┤
│                                                1581074247194257065 │
└────────────────────────────────────────────────────────────────────┘
```
