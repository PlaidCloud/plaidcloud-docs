---
title: H3_GET_RESOLUTION (Lakehouse v1)
description: H3_GET_RESOLUTION — devolve a resolução do índice H3 indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-resolution.md
---

Devolve a resolução do índice [H3](https://eng.uber.com/h3/) indicado. 

## Sintaxe do Analyze

```python
func.h3_get_resolution(h3)
```

## Exemplos do Analyze

```python
func.h3_get_resolution(644325524701193974)

┌────────────────────────────────────────────┐
│ func.h3_get_resolution(644325524701193974) │
├────────────────────────────────────────────┤
│                                         15 │
└────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_GET_RESOLUTION(h3)
```

## Exemplos de SQL

```sql
SELECT H3_GET_RESOLUTION(644325524701193974);

┌───────────────────────────────────────┐
│ h3_get_resolution(644325524701193974) │
├───────────────────────────────────────┤
│                                    15 │
└───────────────────────────────────────┘
```
