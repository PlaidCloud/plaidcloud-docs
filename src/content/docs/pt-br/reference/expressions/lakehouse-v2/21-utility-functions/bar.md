---
title: BAR (Lakehouse v2)
description: "Use a função utilitária BAR no PlaidCloud Lakehouse. Retorna uma string de barra visual que representa um valor dentro de um intervalo. Útil para visualizações baseadas em texto."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

Retorna uma string de barra visual que representa um valor dentro de um intervalo. Útil para visualizações baseadas em texto.

## Sintaxe do Analyze

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Exemplos do Analyze

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## Sintaxe SQL

```sql
BAR(<value>, <min>, <max>, <width>)
```

## Exemplos de SQL

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
