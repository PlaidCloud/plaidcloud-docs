---
title: "PERCENTILE_CONT (Agregação, Lakehouse v2)"
description: PERCENTILE_CONT — devolve um valor de percentil interpolado com base numa distribuição contínua.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-cont.md
---

Devolve um valor de percentil interpolado com base numa distribuição contínua.

## Sintaxe do Analyze

```python
func.percentile_cont(0.5)
```

## Exemplos do Analyze

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## Sintaxe SQL

```sql
PERCENTILE_CONT(0.5)
```

## Exemplos SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
