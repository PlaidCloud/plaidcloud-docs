---
title: ROUND (Lakehouse v2)
description: ROUND — arredonda um número para um número especificado de casas decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

Arredonda um número para um número especificado de casas decimais.

## Sintaxe do Analyze

```python
func.round(<x>[, <d>])
```

## Exemplos do Analyze

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Sintaxe SQL

```sql
ROUND(<x>[, <d>])
```

## Exemplos de SQL

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
