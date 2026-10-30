---
title: LN (Lakehouse v1)
description: LN — devolve o logaritmo natural de x, ou seja, o logaritmo de base e de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

Devolve o logaritmo natural de `x`, ou seja, o logaritmo de base e de `x`. Se x for menor ou igual a 0.0E0, a função devolve NULL.

## Sintaxe do Analyze

```python
func.ln( <x> )
```

## Exemplos do Analyze

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Sintaxe SQL

```sql
LN( <x> )
```

## Exemplos SQL

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
