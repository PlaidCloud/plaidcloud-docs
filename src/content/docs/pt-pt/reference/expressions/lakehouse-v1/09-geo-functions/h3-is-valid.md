---
title: H3_IS_VALID (Lakehouse v1)
description: H3_IS_VALID — verifica se o índice H3 indicado é válido.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

Verifica se o índice [H3](https://eng.uber.com/h3/) indicado é válido.

## Sintaxe do Analyze

```python
func.h3_is_valid(h3)
```

## Exemplos do Analyze

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_IS_VALID(h3)
```

## Exemplos de SQL

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
