---
title: ACOS (Lakehouse v1)
description: ACOS — retorna o arco cosseno de x, ou seja, o valor cujo cosseno é x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

Retorna o arco cosseno de `x`, ou seja, o valor cujo cosseno é `x`. Retorna NULL se `x` não estiver no intervalo de -1 a 1.

## Sintaxe do Analyze

```python
func.abs( <x> )
```

## Exemplos do Analyze

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## Sintaxe SQL

```sql
ACOS( <x> )
```

## Exemplos de SQL

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
