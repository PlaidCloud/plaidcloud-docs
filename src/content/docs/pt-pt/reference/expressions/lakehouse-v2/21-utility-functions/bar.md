---
title: BAR (Lakehouse v2)
description: "Utilize a função utilitária BAR no PlaidCloud Lakehouse. Devolve uma representação de valor em barra, sob a forma de cadeia, dentro de um intervalo. Útil para visualizações baseadas em texto."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

Devolve uma representação visual em barra, sob a forma de cadeia, de um valor dentro de um intervalo. Útil para visualizações baseadas em texto.

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

## Exemplos SQL

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
