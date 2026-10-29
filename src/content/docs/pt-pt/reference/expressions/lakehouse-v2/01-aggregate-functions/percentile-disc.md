---
title: "PERCENTILE_DISC (Agregação, Lakehouse v2)"
description: "Utilize a função de agregação PERCENTILE_DISC no PlaidCloud Lakehouse. Devolve o menor valor cuja distribuição cumulativa é >= ao percentil especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

Devolve o menor valor cuja distribuição cumulativa é >= ao percentil especificado.

## Sintaxe do Analyze

```python
func.percentile_disc(0.5)
```

## Exemplos do Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Sintaxe SQL

```sql
PERCENTILE_DISC(0.5)
```

## Exemplos SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
