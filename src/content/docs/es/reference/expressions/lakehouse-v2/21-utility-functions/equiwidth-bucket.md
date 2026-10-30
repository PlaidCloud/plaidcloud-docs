---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "Use la función de utilidad EQUIWIDTH_BUCKET en PlaidCloud Lakehouse. Devuelve el número de intervalo de un valor en un histograma de ancho uniforme. Divide el rango [min, max] en intervalos de igual ancho."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

Devuelve el número de intervalo de un valor en un histograma de ancho uniforme. Divide el rango [min, max] en intervalos de igual ancho.

## Sintaxis de Analyze

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Ejemplos de Analyze

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## Sintaxis de SQL

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## Ejemplos de SQL

```sql
SELECT score, EQUIWIDTH_BUCKET(score, 0, 100, 10) AS bucket
FROM students;

┌───────┬────────┐
│ score │ bucket │
├───────┼────────┤
│    25 │      3 │
│    75 │      8 │
│    95 │     10 │
└───────┴────────┘
```
