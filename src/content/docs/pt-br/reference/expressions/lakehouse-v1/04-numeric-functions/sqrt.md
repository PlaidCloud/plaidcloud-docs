---
title: SQRT (Lakehouse v1)
description: SQRT — retorna a raiz quadrada de um número não negativo x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

Retorna a raiz quadrada de um número não negativo `x`. Retorna NaN para entradas negativas.

## Sintaxe do Analyze

```python
func.sqrt( <x> )
```

## Exemplos do Analyze

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## Sintaxe SQL

```sql
SQRT( <x> )
```

## Exemplos de SQL

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
