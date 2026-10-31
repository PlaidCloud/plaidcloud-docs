---
title: H3_IS_VALID (Lakehouse v1)
description: H3_IS_VALID — comprueba si el índice H3 dado es válido.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

Comprueba si el índice [H3](https://eng.uber.com/h3/) dado es válido.

## Sintaxis de Analyze

```python
func.h3_is_valid(h3)
```

## Ejemplos de Analyze

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_IS_VALID(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
