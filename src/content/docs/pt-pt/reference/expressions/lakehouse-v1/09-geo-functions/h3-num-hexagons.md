---
title: H3_NUM_HEXAGONS (Lakehouse v1)
description: H3_NUM_HEXAGONS — devolve o número de índices H3 únicos na resolução indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

Devolve o número de índices [H3](https://eng.uber.com/h3/) únicos na resolução indicada. 

## Sintaxe do Analyze

```python
func.h3_num_hexagons(res)
```

## Exemplos do Analyze

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
H3_NUM_HEXAGONS(res)
```

## Exemplos de SQL

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
