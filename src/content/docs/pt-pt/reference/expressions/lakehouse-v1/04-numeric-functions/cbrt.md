---
title: CBRT (Lakehouse v1)
description: CBRT — devolve a raiz cúbica de um número não negativo x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

Devolve a raiz cúbica de um número não negativo `x`.

## Sintaxe do Analyze

```python
func.cbrt( <x> )
```

## Exemplos do Analyze

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## Sintaxe SQL

```sql
CBRT( <x> )
```

## Exemplos SQL

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
