---
title: H3_GET_UNIDIRECTIONAL_EDGE
---

Returns the edge between the given two [H3](https://eng.uber.com/h3/) indexes.

## Analyze Syntax

```python
func.h3_get_unidirectional_edge(h3, a_h3)
```

## Analyze Examples

```python
func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754)

┌─────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├─────────────────────────────────────────────────────────────────────────┤
│                                                     1581074247194257065 │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_UNIDIRECTIONAL_EDGE(h3, a_h3)
```

## SQL Examples

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE(644325524701193897, 644325524701193754);

┌────────────────────────────────────────────────────────────────────┐
│ h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├────────────────────────────────────────────────────────────────────┤
│                                                1581074247194257065 │
└────────────────────────────────────────────────────────────────────┘
```