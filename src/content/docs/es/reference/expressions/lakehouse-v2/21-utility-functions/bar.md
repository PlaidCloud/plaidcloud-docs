---
title: BAR (Lakehouse v2)
description: "Use la función de utilidad BAR en PlaidCloud Lakehouse. Devuelve una representación visual de barra, en forma de cadena, de un valor dentro de un rango. Es útil para visualizaciones basadas en texto."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

Devuelve una representación visual de barra, en forma de cadena, de un valor dentro de un rango. Es útil para visualizaciones basadas en texto.

## Sintaxis de Analyze

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Ejemplos de Analyze

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
BAR(<value>, <min>, <max>, <width>)
```

## Ejemplos de SQL

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
