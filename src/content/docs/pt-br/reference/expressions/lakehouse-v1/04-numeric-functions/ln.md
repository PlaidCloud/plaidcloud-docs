---
title: LN (Lakehouse v1)
description: LN — retorna o logaritmo natural de x, ou seja, o logaritmo de x na base e.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

Retorna o logaritmo natural de `x`, ou seja, o logaritmo de `x` na base e. Se x for menor ou igual a 0.0E0, a função retorna NULL.

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

## Exemplos de SQL

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
