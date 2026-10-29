---
title: "PERCENTILE_DISC (Percentil, Lakehouse v2)"
description: "Utilize a função de percentil PERCENTILE_DISC no PlaidCloud Lakehouse. Devolve o menor valor cuja distribuição cumulativa é >= ao percentil especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

Devolve o menor valor cuja distribuição cumulativa é >= ao percentil especificado.

## Sintaxe de Analyze

```python
func.percentile_disc(<percentile>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
