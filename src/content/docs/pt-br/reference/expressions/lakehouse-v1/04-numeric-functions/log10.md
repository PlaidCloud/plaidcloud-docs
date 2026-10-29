---
title: LOG10 (Lakehouse v1)
description: LOG10 — retorna o logaritmo de x na base 10. Referência.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

Retorna o logaritmo de `x` na base 10. Se `x` for menor ou igual a 0.0E0, a função retorna NULL.


## Sintaxe do Analyze

```python
func.log10( <x> )
```

## Exemplos do Analyze

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## Sintaxe SQL

```sql
LOG10( <x> )
```

## Exemplos de SQL

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
