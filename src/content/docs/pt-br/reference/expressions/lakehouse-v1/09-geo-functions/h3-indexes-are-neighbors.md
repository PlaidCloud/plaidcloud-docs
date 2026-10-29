---
title: H3_INDEXES_ARE_NEIGHBORS (Lakehouse v1)
description: H3_INDEXES_ARE_NEIGHBORS — retorna se os índices H3 informados são ou não vizinhos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-indexes-are-neighbors.md
---

Retorna se os índices [H3](https://eng.uber.com/h3/) informados são ou não vizinhos.

## Sintaxe do Analyze

```python
func.h3_indexes_are_neighbors(h3, a_h3)
```

## Exemplos do Analyze

```python
func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897)

┌───────────────────────────────────────────────────────────────────────┐
│ func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├───────────────────────────────────────────────────────────────────────┤
│ true                                                                  │
└───────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_INDEXES_ARE_NEIGHBORS(h3, a_h3)
```

## Exemplos de SQL

```sql
SELECT H3_INDEXES_ARE_NEIGHBORS(644325524701193974, 644325524701193897);

┌──────────────────────────────────────────────────────────────────┐
│ h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├──────────────────────────────────────────────────────────────────┤
│ true                                                             │
└──────────────────────────────────────────────────────────────────┘
```
