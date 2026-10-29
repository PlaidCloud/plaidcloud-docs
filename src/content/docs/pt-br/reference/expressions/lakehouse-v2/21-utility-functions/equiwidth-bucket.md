---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "Use a função utilitária EQUIWIDTH_BUCKET no PlaidCloud Lakehouse. Retorna o número do intervalo de um valor em um histograma de largura igual. Divide o intervalo [min."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

Retorna o número do intervalo de um valor em um histograma de largura igual. Divide o intervalo [min, max] em faixas de larguras iguais.

## Sintaxe do Analyze

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Exemplos do Analyze

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## Sintaxe SQL

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## Exemplos de SQL

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
