---
title: H3_NUM_HEXAGONS (Lakehouse v1)
description: H3_NUM_HEXAGONS — zwraca liczbę unikatowych indeksów H3 dla danej rozdzielczości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

Zwraca liczbę unikatowych indeksów [H3](https://eng.uber.com/h3/) dla danej rozdzielczości. 

## Składnia Analyze

```python
func.h3_num_hexagons(res)
```

## Przykłady Analyze

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## Składnia SQL

```sql
H3_NUM_HEXAGONS(res)
```

## Przykłady SQL

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
