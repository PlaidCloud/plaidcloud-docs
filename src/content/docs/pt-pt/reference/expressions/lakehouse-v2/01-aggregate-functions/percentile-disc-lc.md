---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC — devolve o valor de percentil através de um algoritmo otimizado para baixa cardinalidade.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

Devolve o valor de percentil através de um algoritmo otimizado para baixa cardinalidade.

## Sintaxe do Analyze

```python
func.percentile_disc_lc(0.5)
```

## Exemplos do Analyze

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Sintaxe SQL

```sql
PERCENTILE_DISC_LC(0.5)
```

## Exemplos SQL

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
