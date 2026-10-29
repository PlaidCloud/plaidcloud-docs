---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "Użyj funkcji narzędziowej EQUIWIDTH_BUCKET w PlaidCloud Lakehouse. Zwraca numer przedziału dla wartości w histogramie o równej szerokości przedziałów. Dzieli zakres [min, max] na przedziały o równej szerokości."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

Zwraca numer przedziału dla wartości w histogramie o równej szerokości przedziałów. Dzieli zakres [min, max] na przedziały o równej szerokości.

## Składnia Analyze

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Przykłady Analyze

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## Składnia SQL

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## Przykłady SQL

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
