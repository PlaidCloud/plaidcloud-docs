---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID
---

Determines if the provided H3Index is a valid unidirectional edge index. Returns 1 if it's a unidirectional edge and 0 otherwise.

## Analyze Syntax

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Analyze Examples

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## SQL Examples

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```