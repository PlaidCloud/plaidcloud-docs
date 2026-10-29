---
title: SQRT (Lakehouse v1)
description: SQRT — devolve a raiz quadrada de um número não negativo x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

Devolve a raiz quadrada de um número não negativo `x`. Devolve NaN para valores de entrada negativos.

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

## Exemplos SQL

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```
