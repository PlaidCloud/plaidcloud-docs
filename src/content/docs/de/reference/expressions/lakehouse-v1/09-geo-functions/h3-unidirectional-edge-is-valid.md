---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID (Lakehouse v1)
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — bestimmt, ob der angegebene H3Index ein gültiger Index einer gerichteten Kante ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

Bestimmt, ob der angegebene H3Index ein gültiger Index einer gerichteten Kante ist. Gibt 1 zurück, wenn es sich um eine gerichtete Kante handelt, andernfalls 0.

## Analyze-Syntax

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Analyze-Beispiele

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## SQL-Beispiele

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
