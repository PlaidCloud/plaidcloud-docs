---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "Verwenden Sie die Hilfsfunktion EQUIWIDTH_BUCKET in PlaidCloud Lakehouse. Gibt die Bucket-Nummer eines Werts in einem Histogramm mit gleich breiten Intervallen zurück. Teilt den Bereich [min."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

Gibt die Bucket-Nummer eines Werts in einem Histogramm mit gleich breiten Intervallen zurück. Teilt den Bereich [min, max] in Intervalle gleicher Breite.

## Analyze-Syntax

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Analyze-Beispiele

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## SQL-Syntax

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## SQL-Beispiele

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
