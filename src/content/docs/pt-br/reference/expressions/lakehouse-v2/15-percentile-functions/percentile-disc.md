---
title: "PERCENTILE_DISC (Percentil, Lakehouse v2)"
description: "Use a função de percentil PERCENTILE_DISC no PlaidCloud Lakehouse. Retorna o menor valor cuja distribuição cumulativa é maior ou igual ao percentil especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

Retorna o menor valor cuja distribuição cumulativa é >= o percentil especificado.

## Sintaxe do Analyze

```python
func.percentile_disc(<percentile>)
```

## Exemplos do Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## Sintaxe SQL

```sql
PERCENTILE_DISC(<percentile>)
```

## Exemplos de SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
