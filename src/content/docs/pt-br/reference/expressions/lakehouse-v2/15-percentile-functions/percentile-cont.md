---
title: "PERCENTILE_CONT (Percentil, Lakehouse v2)"
description: PERCENTILE_CONT — retorna um valor de percentil interpolado com base em uma distribuição contínua.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

Retorna um valor de percentil interpolado com base em uma distribuição contínua.

## Sintaxe do Analyze

```python
func.percentile_cont(<percentile>)
```

## Exemplos do Analyze

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## Sintaxe SQL

```sql
PERCENTILE_CONT(<percentile>)
```

## Exemplos de SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
