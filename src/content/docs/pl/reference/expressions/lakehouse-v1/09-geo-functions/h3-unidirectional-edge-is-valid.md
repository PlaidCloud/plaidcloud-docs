---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID (Lakehouse v1)
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — określa, czy podany indeks H3Index jest prawidłową krawędzią jednokierunkową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

Określa, czy podany indeks H3Index jest prawidłowym indeksem krawędzi jednokierunkowej. Zwraca 1, jeśli jest to krawędź jednokierunkowa, a w przeciwnym razie 0.

## Składnia Analyze

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Przykłady Analyze

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## Przykłady SQL

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
