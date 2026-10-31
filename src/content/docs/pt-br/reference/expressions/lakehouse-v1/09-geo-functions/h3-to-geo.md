---
title: H3_TO_GEO (Lakehouse v1)
description: H3_TO_GEO — retorna a longitude e a latitude correspondentes ao índice H3 informado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-geo.md
---

Retorna a longitude e a latitude correspondentes ao índice [H3](https://eng.uber.com/h3/) informado. 

## Sintaxe do Analyze

```python
func.h3_to_geo(h3)
```

## Exemplos do Analyze

```python
func.h3_to_geo(644325524701193974)

┌────────────────────────────────────────┐
│   func.h3_to_geo(644325524701193974)   │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_TO_GEO(h3)
```

## Exemplos de SQL

```sql
SELECT H3_TO_GEO(644325524701193974);

┌────────────────────────────────────────┐
│      h3_to_geo(644325524701193974)     │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```
