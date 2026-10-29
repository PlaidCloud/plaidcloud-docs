---
title: LOG(x) (Lakehouse v1)
description: LOG(x) — retorna o logaritmo natural de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

Retorna o logaritmo natural de `x`. Se x for menor ou igual a 0.0E0, a função retorna NULL.

## Sintaxe do Analyze

```python
 func.log( <x> )
```

## Exemplos do Analyze

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Sintaxe SQL

```sql
LOG( <x> )
```

## Exemplos de SQL

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
