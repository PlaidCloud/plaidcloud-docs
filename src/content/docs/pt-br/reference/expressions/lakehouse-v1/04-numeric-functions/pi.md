---
title: PI (Lakehouse v1)
description: PI — retorna o valor de π como um valor de ponto flutuante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

Retorna o valor de π como um valor de ponto flutuante.

## Sintaxe do Analyze

```python
func.pi()
```

## Exemplos do Analyze

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## Sintaxe SQL

```sql
PI()
```

## Exemplos de SQL

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
