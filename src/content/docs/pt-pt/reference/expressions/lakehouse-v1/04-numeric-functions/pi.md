---
title: PI (Lakehouse v1)
description: PI — devolve o valor de π como um valor de vírgula flutuante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

Devolve o valor de π como um valor de vírgula flutuante.

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

## Exemplos SQL

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
